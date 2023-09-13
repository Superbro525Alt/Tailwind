import os, sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import socket, tailwindall.network_lib.server as server





class LANDatabase(server.LANServer):
    def __init__(self, port, data_store_path=None):
        self.data_store_path = data_store_path

        if self.data_store_path is None:
            self.data = {}
        else:
            with open(self.data_store_path, "r") as f:
                self.data = eval(f.read())

        super().__init__(port, self.respond)

    def respond(self, data):
        op = data.split("|")[0].strip()

        if op == "get":
            key = data.split("|")[1].lstrip()

            # the path will be in terms of path/to/data which corresponds to self.data["path"]["to"]["data"]
            path = key.split("/")
            value = self.data
            for p in path:
                value = value[p]

            if value is None:
                return "None"
            return str(value)

        elif op == "set":
            key = data.split("|")[1].lstrip()

            # the path will be in terms of path/to/data which corresponds to self.data["path"]["to"]["data"]
            path = key.split("/")
            value = self.data
            s = data.split("|")[2].lstrip()

            res = "Success"

            for p in path:
                if p not in value:
                    if p == path[-1]:
                        if type(value) == str:
                            res = "Error: Final location has already been set as a string"
                            break
                        value[p] = s
                        break
                    else:
                        value[p] = {}

                if type(value) == str:
                    res = "Error: Location has already been set as a string"
                    break
                else:
                    value = value[p]


            if self.data_store_path is not None:
                with open(self.data_store_path, "w") as f:
                    f.write(str(self.data))

            return res
