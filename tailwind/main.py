import os
import sys
from time import sleep
from tailwind.window import Window
from tailwind.widgets import *
import tailwind.util as util

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/lib")

if util.is_main_thread(__name__):
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
                        os.system(f"cd {root} && git add . && git commit -m \"Initial Commit\" && git push origin master")

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


    props = util.WindowProperties(dynamic_scaling=True, dev_resolution=util.resolution(1920, 1080))

    window = Window(None, "Project Creator", props, False, debug=True, onTick=onTick)

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
