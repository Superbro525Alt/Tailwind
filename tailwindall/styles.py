import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import tailwindall.util as util

class Styles:
    @classmethod
    def parse(cls, style: str, file=False):
        # parse a css file into a dictionary using the framework {"classes": {"class_name": {"property": "value"}}, "ids": {"id_name": {"property": "value"}}, "tags": {"tag_name": {"property": "value"}}}
        # this is a very basic parser, it only supports the following syntax:
        # .class_name {property: value;}
        # #id_name {property: value;}
        # tag_name {property: value;}

        # remove comments
        if file:
            style = util.read_file(style, {"strip": True})
        if style != "" and style != None:
            style = style.strip()
            style = cls.remove_comments(style)

            _style = {"classes": {}, "ids": {}, "tags": {}}


            for line in style.split("\n"):
                # remove whitespace
                line = line.strip()
                if line == "":
                    # if the line is empty, skip it
                    continue
                elif line[0] == ".":
                    # if the line is a class, add it to the classes dictionary
                    _style = cls.add_class(line, style, _style)
                elif line[0] == "#":
                    # if the line is an id, add it to the ids dictionary
                    _style = cls.add_id(line, style, _style)
                else:
                    # if the line is a tag, add it to the tags dictionary
                    _style = cls.add_tag(line, style, _style)

            return util.Style(_style["classes"], _style["tags"], _style["ids"])

    @classmethod
    def remove_comments(cls, style):
        # remove comments from a css file. Comments are denoted by /* and */ and can span multiple lines

        # find the first comment
        comment_start = style.find("/*")
        if comment_start == -1:
            # if there are no comments, return the style
            return style
        else:
            # find the end of the comment
            comment_end = style.find("*/")
            if comment_end == -1:
                # if there is no end to the comment, return the style
                return style
            else:
                # remove the comment and return the style
                return cls.remove_comments(style[:comment_start] + style[comment_end + 2:])

    @classmethod
    def add_class(cls, line, style, _style_):
        # add a class to the classes dictionary
        _style = {}
        # find the end of the class name
        class_end = line.find(" ")
        if class_end == -1:
            # if there is no end to the class name, return
            return _style
        else:
            # get the class name
            class_name = line[1:class_end]
            # find the end of the class
            class_end = line.find("}")
            if class_end == -1:
                # if there is no end to the class, return
                return
            else:
                # get the class
                class_ = line[line.find("{") + 1:class_end]
                # add the class to the classes dictionary
                _style_["classes"][class_name] = cls.parse_class(class_, style)

                # return the style
                return _style_

    @classmethod
    def parse_class(cls, class_, style):
        # parse a class into a dictionary using the framework {"property": "value"}
        _style = {}
        for line in class_.split(";"):
            # remove whitespace
            line = line.strip()
            if line == "":
                # if the line is empty, skip it
                continue
            else:
                # find the end of the property
                property_end = line.find(":")
                if property_end == -1:
                    # if there is no end to the property, return
                    return
                else:
                    # get the property
                    property_ = line[:property_end]
                    # get the value
                    value = line[property_end + 1:]
                    # add the property to the class
                    _style[property_] = value

        # return the style
        return _style

    @classmethod
    def add_id(cls, line, style, _style_):
    # add an id to the ids dictionary
        _style = {}
        # find the end of the id name
        id_end = line.find(" ")
        if id_end == -1:
            # if there is no end to the id name, return
            return _style
        else:
            # get the id name
            id_name = line[1:id_end]
            # find the end of the id
            id_end = line.find("}")
            if id_end == -1:
                # if there is no end to the id, return
                return
            else:
                # get the id
                id_ = line[line.find("{") + 1:id_end]
                # add the id to the ids dictionary
                _style_["ids"][id_name] = cls.parse_id(id_, style)

                # return the style
                return _style_

    @classmethod
    def parse_id(cls, id_, style):
        # parse an id into a dictionary using the framework {"property": "value"}
        _style = {}
        for line in id_.split(";"):
            # remove whitespace
            line = line.strip()
            if line == "":
                # if the line is empty, skip it
                continue
            else:
                # find the end of the property
                property_end = line.find(":")
                if property_end == -1:
                    # if there is no end to the property, return
                    return
                else:
                    # get the property
                    property_ = line[:property_end]
                    # get the value
                    value = line[property_end + 1:]
                    # add the property to the id
                    _style[property_] = value

        # return the style
        return _style

    @classmethod
    def add_tag(cls, line, style, _style_):
        # add a tag to the tags dictionary
        _style = {}
        # find the end of the tag name
        tag_end = line.find(" ")
        if tag_end == -1:
            # if there is no end to the tag name, return
            return _style
        else:
            # get the tag name
            tag_name = line[:tag_end]
            # find the end of the tag
            tag_end = line.find("}")
            if tag_end == -1:
                # if there is no end to the tag, return
                return
            else:
                # get the tag
                tag = line[line.find("{") + 1:tag_end]
                # add the tag to the tags dictionary
                _style_["tags"][tag_name] = cls.parse_tag(tag, style)

                # return the style
                return _style_

    @classmethod
    def parse_tag(cls, tag, style):
        # parse a tag into a dictionary using the framework {"property": "value"}
        _style = {}
        for line in tag.split(";"):
            # remove whitespace
            line = line.strip()
            if line == "":
                # if the line is empty, skip it
                continue
            else:
                # find the end of the property
                property_end = line.find(":")
                if property_end == -1:
                    # if there is no end to the property, return
                    return
                else:
                    # get the property
                    property_ = line[:property_end]
                    # get the value
                    value = line[property_end + 1:]
                    # add the property to the tag
                    _style[property_] = value

        # return the style
        return _style