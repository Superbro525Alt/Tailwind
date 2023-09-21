class BaseObject:
    """
    The base object for all objects in the library.

    This class is used to override the default methods of the object class.

    :param args: The arguments.
    :param kwargs: The keyword arguments.

    :return: A base object.
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