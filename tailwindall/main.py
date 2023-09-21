import os
import sys
import threading
from time import sleep

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from tailwindall.window import Window
from tailwindall.widgets import *
import tailwindall.util as util
import tailwindall.widget as widget
import tailwindall.bases as bases

import tailwindall.network_lib.client as client
import tailwindall.network_lib.server as server
import tailwindall.network_lib.network as network
import tailwindall.network_lib.database as database

import tailwindall.graphics_lib.graphics as graphics

import tailwindall.maths_lib.shapes as shapes
import tailwindall.maths_lib.angles as angles

import tailwindall.styles as styles

import tailwindall.statistics_lib.statistics as statistics
import tailwindall.statistics_lib.diagrams as diagrams

import tailwindall.graphing as graphing

import tailwindall.web_lib.web as web
import tailwindall.web_lib.js as js
import tailwindall.web_lib.components as components


def window_test():
    def create():
        root = project_root.get_value()

        if not create_git.get_value():
            os.system(f"cd {root} && git clone {git_origin.get_value()} .")
            return

        if project_type.get_value() == "Python":
            # get the parent directory of root
            if True:
                # create a repo using repository_name.get_value()
                os.system(f"cd {root} && git clone {git_origin.get_value()} . && mkdir {repository_name.get_value()}")
                with open(f"{root}/.gitignore", "w+") as f:
                    f.write(".idea\n.vscode")

                with open(f"{root}/README.md", "w+") as f:
                    f.write("# " + repository_name.get_value())

                with open(f"{root}/LICENSE.md", "w+") as f:
                    f.write("""# MIT License 

    Copyright (c) 2023

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    """)

                    with open(f"{root}/requirements.txt", "w+") as f:
                        f.write("")

                    os.system(f"cd {root} && mkdir {repository_name.get_value()}")

                    with open(f"{root}/{repository_name.get_value()}/{main_file_name.get_value()}", "w+") as f:
                        f.write("")

                    os.system(f"cd {root} && mkdir .github && cd .github && mkdir workflows")
                    with open(f"{root}/.github/workflows/python-app.yml", "w+") as f:
                        f.write(f"""# This workflow will install Python dependencies, run tests and lint with a single version of Python
    # For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

    name: Run

    on:
      push:
        branches: [ "master", "dev" ]
      pull_request:
        branches: [ "master" ]

    permissions:
      contents: read

    jobs:
      build-on-linux:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.11
          uses: actions/setup-python@v3
          with:
            python-version: "3.11"
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        - name: Lint with flake8
          run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        - name: Test with python 3.11
          run: |
            python {repository_name.get_value()}/main.py

    """)
                        os.system(
                            f"cd {root} && git add . && git commit -m \"Initial Commit\" && git push origin master")

                        os.system(f"cd {root} && git branch dev && git checkout dev && git push origin dev")

    def onTick(_window: Window, *args, **kwargs):
        [i.hide() for i in PYTHON_INPUTS]
        if project_type.get_value() == "Python":
            [i.show() for i in PYTHON_INPUTS]
            if create_git.get_value() == False:
                repository_name.hide()

                main_file_name.hide()
            else:
                repository_name.show()

                main_file_name.show()

    props = util.WindowProperties(dynamic_scaling=True, dev_resolution=util.resolution(1920, 1080),
                                  secondary_window=True, secondary_window_framework="pygame")

    window = Window(None, "Project Creator", props, debug=True, onTick=onTick)

    project_type = Dropdown(window, ["Python", "Next.js", "React", "React Native", "Rust"], util.Style.empty(), {}, {})

    window.add_widget(project_type, util.PlaceData(0.3, 0.1, util.CenterAnchor().get_anchor()))

    create_git = Checkbox(window, "Create Repository", util.Style.empty(), {}, {})

    window.add_widget(create_git, util.PlaceData(0.7, 0.1, util.CenterAnchor().get_anchor()))

    git_origin = Entry(window, "Git Origin", util.Style.empty(), {}, {})

    window.add_widget(git_origin, util.PlaceData(0.3, 0.2, util.CenterAnchor().get_anchor()))

    repository_name = Entry(window, "Repository Name", util.Style.empty(), {}, {})

    window.add_widget(repository_name, util.PlaceData(0.7, 0.2, util.CenterAnchor().get_anchor()))

    repository_name.hide()

    create_project = Button(window, lambda: create(), util.Style.empty(), {}, {}, text="Create Project")

    window.add_widget(create_project, util.PlaceData(0.5, 0.8, util.CenterAnchor().get_anchor()))

    project_root_label = Label(window, "Not Selected", util.Style.empty(), {}, {})

    window.add_widget(project_root_label, util.PlaceData(0.7, 0.3, util.CenterAnchor().get_anchor()))

    project_root = FolderSelect(window, project_root_label, "Project Root", "/", "Project Root", util.Style.empty(), {},
                                {})

    window.add_widget(project_root, util.PlaceData(0.3, 0.3, util.CenterAnchor().get_anchor()))

    main_file_name = Entry(window, "Main File Name", util.Style.empty(), {}, {})

    window.add_widget(main_file_name, util.PlaceData(0.5, 0.4, util.CenterAnchor().get_anchor()))

    PYTHON_INPUTS = [

    ]

    window.main_loop()


def database_client_test():
    d = database.LANDatabase(65053)

    d.start()

    c = client.LANClient(d.host, 65053)

    c.connect()

    # c.send("set|path/to/data|test3")
    c.send(network.Request("set", "path/to/data", "test3"))
    print(c.send(network.Request("get", "path/to/data")))

    d.close()


def website_test():
    w = web.Website("Test", 65053)

    w.route("/test", web.Page([
        components.Button("Click Me", js.redirect("/"))
    ], w, "test"))

    w.route("/", web.Page([
        components.Button("Click Me", js.redirect("/test")),
        components.Div([
            components.H1("Hello World"),
            components.Text("This is a test")
        ]),
        components.Div([
            components.H1("Hello World"),
            components.Text("This is a test")
        ]),
        components.Table([
            "Heading 1",
            "Heading 2"
        ], [
            [
                "Row 1",
                "Row 1"
            ],
            [
                "Row 2",
                "Row 2"
            ]
        ]),
        components.Div([
            components.H1("Hello World"),
            components.Input("text"),
            components.Link("Click Me", "/test")
        ])
    ], w, "Home", _tw="script.tw", stylesheet="style.tw"))

    w.run(dev=True)


if util.is_main_thread(__name__):
    # if not on a server
    if os.environ.get("SSH_CLIENT") is None:
        pass