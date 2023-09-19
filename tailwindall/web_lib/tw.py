DEFAULT_CSS = """
body {
    background-color: #000000;
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    margin: 0;
    padding: 0;
}

h1 {
    font-size: 32px;
}

h2 {
    font-size: 24px;
}

h3 {
    font-size: 20px;
}

h4 {
    font-size: 18px;
}

h5 {
    font-size: 16px;
}

h6 {
    font-size: 14px;
}

p {
    font-size: 16px;
}

a {
    color: #ffffff;
    text-decoration: none;
}

a:hover {
    color: #ffffff;
    text-decoration: underline;
}

button {
    background-color: #000000;
    border: 0;
    color: #ffffff;
    cursor: pointer;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    margin: 0;
    padding: 0;
}

button:hover {
    background-color: #ffffff;
    color: #000000;
}

table {
    border-collapse: collapse;
    border-spacing: 0;
    border: 1px solid #ffffff;
}

table, th, td {
    border: 1px solid #ffffff;
}

th, td {
    padding: 5px;
    text-align: left;
}

th {
    background-color: #000000;
    color: #ffffff;
}

td {
    background-color: #ffffff;
    color: #000000;
}

input {
    background-color: #ffffff;
    border: 1px solid #000000;
    color: #000000;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    margin: 0;
    padding: 0;
}
"""

def parse(tw, app):
    ret = tw
    if tw.startswith('"web script"'):
        ret = tw[12:]
        file_import = []
        functions = []
        # find each line that starts with using
        for line in ret.split("\n"):
            if line.startswith("using"):
                # get the file name
                file_import.append(line.split(" ")[1])
            elif line.startswith("def"):
                functions.append(line.split(" ")[1])


        for _import in file_import:
            file = open(f"{_import}.js", "r")
            i = file.read()
            if i.startswith('"module"'):
                i = i[8:]
                app.route_plain(f"/_tw/modules/{_import}.js", i, "text/javascript")
                file.close()
            else:
                raise Exception("Invalid js module file")

            ret = ret.replace(f"using {_import}", f'import * as {_import} from "/_tw/modules/{_import}.js"')


        for function in functions:
            ret = ret.replace(f"def {function}", f"function {function}")

        ret = ret.replace("print", "console.log")

        app.route_plain("/_tw/_main.js", ret)
    elif tw.startswith('"web style"'):
        ret = tw[11:]
        app.route_plain("/_tw/_style/_main.css", ret, "text/css")
    else:
        raise Exception('"Invalid tw web file must start with: \"web script\" or \"web style\"')


