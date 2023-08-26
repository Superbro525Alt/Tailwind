def _is(this, other):
    return isinstance(this, other)

def read_file(file, options={}):
    # read a file and return its contents
    try:
        with open(file, "r") as f:
            if options["strip"] if "strip" in options else False:
                return f.read().strip()
            if options["lines"] if "lines" in options else False:
                return f.readlines()
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("File not found: " + file)