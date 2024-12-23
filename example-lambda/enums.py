from enum import Enum, EnumMeta
from typing import Union, Any

from abc import ABCMeta, abstractmethod


# class ABCEnumMeta(ABCMeta, EnumMeta):
#     @classmethod
#     @abstractmethod
#     def get_by_id(cls, code: int) -> Any:
#         pass

#     @classmethod
#     @abstractmethod
#     def get_by_val(cls, val: str) -> Any:
#         pass


class UserType(Enum):
    PRIVATE = 1, "Private"
    FREELANCE = 2, "Freelance"
    CORPORATE = 3, "Corporate"

    def __init__(self, code: int, value: str):
        self.code = code
        self.val = value

    @classmethod
    def get_by_id(cls, code: int) -> Union["UserType", None]:
        return next((member for member in cls if member.code == code), None)

    @classmethod
    def get_by_val(cls, val: str) -> Union["UserType", None]:
        return next((member for member in cls if member.val == val), None)


class Encoding(Enum):
    UTF_8 = 1, "UTF-8"

    def __init__(self, code: int, value: str):
        self.code = code
        self.val = value

    @classmethod
    def get_by_id(cls, code: int) -> Union["Encoding", None]:
        return next((member for member in cls if member.code == code), None)

    @classmethod
    def get_by_val(cls, val: str) -> Union["Encoding", None]:
        return next((member for member in cls if member.val == val), None)


class NewLine(Enum):
    CR = 1, "\r"
    LF = 2, "\n"
    CRLF = 3, "\r\n"

    def __init__(self, code: int, value: str):
        self.code = code
        self.val = value

    @classmethod
    def get_by_id(cls, code: int) -> Union["NewLine", None]:
        return next((member for member in cls if member.code == code), None)

    @classmethod
    def get_by_val(cls, val: str) -> Union["NewLine", None]:
        return next((member for member in cls if member.val == val), None)
