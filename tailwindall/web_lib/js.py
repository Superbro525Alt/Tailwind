def redirect(place: str):
    return "window.location.href = \"" + place + "\""

def reload():
    return "window.location.reload()"

def alert(text: str):
    return "alert(\"" + text + "\")"

def confirm(text: str):
    return "confirm(\"" + text + "\")"

def prompt(text: str):
    return "prompt(\"" + text + "\")"

def log(text: str):
    return "console.log(\"" + text + "\")"

def error(text: str):
    return "console.error(\"" + text + "\")"

def warn(text: str):
    return "console.warn(\"" + text + "\")"

def info(text: str):
    return "console.info(\"" + text + "\")"

def debug(text: str):
    return "console.debug(\"" + text + "\")"

def table(text: str):
    return "console.table(\"" + text + "\")"

def clear():
    return "console.clear()"