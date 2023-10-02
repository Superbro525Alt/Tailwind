from typing import overload


class BaseObject:
    """
    The base object for all objects in the library.

    This class is used to override the default methods of the object class.

    :var None:

    :param args: The arguments.
    :param kwargs: The keyword arguments.

    :return: A base object used for inheritance
    """
    def __str__(self) -> str:
        return f"{self.__class__.__name__}({', '.join([f'{key}={value}' for key, value in self.__dict__.items()])})"

    def __eq__(self, other) -> bool:
        if type(other) == type(self):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __gt__(self, other) -> bool:
        raise Exception("Cannot compare objects")

    def __lt__(self, other) -> bool:
        raise Exception("Cannot compare objects")

    def __ge__(self, other) -> bool:
        raise Exception("Cannot compare objects")

    def __le__(self, other) -> bool:
        raise Exception("Cannot compare objects")

    def __add__(self, other) -> float:
        raise Exception("Cannot add objects")

    def __sub__(self, other) -> float:
        raise Exception("Cannot subtract objects")

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb)  -> None:
        pass

    def __del__(self)  -> None:
        pass

    def __init__(self, *args, **kwargs) -> None:
        pass

class Constants(BaseObject):
    """
    A constants object.

    Stores constants for a program like a manager.

    Can return a value from the constants or set a value in the constants.


    :var constants: The constants.

    :param initial: The initial constants.
    :param args: The arguments.
    :param kwargs: The keyword arguments.

    :return: A constants object.
    """
    def __init__(self, initial: dict, *args, **kwargs) -> None:
        self.constants = initial


    def get_value(self, key: str) -> any:
        """
        Gets a value from the constants.

        :param key: The key.
        :return: The value.
        """
        return self.constants[key]

    def set_value(self, key: str, value: any) -> None:
        """
        Sets a value in the constants.

        :param key: The key.
        :param value: The value.
        :return: None
        """
        self.constants[key] = value

class Rules(BaseObject):
    """
    A rules object.

    Allows the passing of a list of IDS and will return the corresponding values


    :param rules: The rules (a dictionary with a lost of ints as the ids and an output as the value)
    :param args: The arguments.
    :param kwargs: The keyword arguments.

    :return: A rules object.
    """

    def __init__(self, rules: dict, id_to_text: dict, *args, **kwargs) -> None:
        self.rules = rules
        self.id_to_text = id_to_text

    def get_result(self, ids: list[int]) -> any:
        """
        Gets the result from the rules.

        :param ids: The ids.
        :return: The result.
        """

        if tuple(ids) in self.rules:
            return self.rules[tuple(ids)]
        return None

    def add_rule(self, ids: list[int], result: any) -> None:
        """
        Adds a rule to the rules.

        :param ids: The ids.
        :param result: The result.
        :return: None
        """
        self.rules[ids] = result

    def remove_rule(self, ids: list[int]) -> None:
        """
        Removes a rule from the rules.

        :param ids: The ids.
        :return: None
        """
        del self.rules[ids]


    def get_text(self, _id: int | list[int]) -> str | list[str]:
        """
        Gets the text from the id.

        :param _id: The id.
        :return: The text.
        """

        if type(_id) == list:
            return "\n".join([self.id_to_text[id] for id in _id]) if len(_id) > 0 else "No proofs"
        return self.id_to_text[_id]

    def add_text(self, _id: int, text: str) -> None:
        """
        Adds a text to the rules.

        :param _id: The id.
        :param text: The text.
        :return: None
        """
        self.id_to_text[_id] = text

    def remove_text(self, _id: int) -> None:
        """
        Removes a text from the rules.

        :param _id: The id.
        :return: None
        """
        del self.id_to_text[_id]
