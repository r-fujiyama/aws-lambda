from enum import Enum
from typing import Union


class Encode(Enum):
    UTF_8 = 1, "UTF-8"

    def __init__(self, code: int, value: str):
        self.code = code
        self.val = value

    @classmethod
    def get_by_id(cls, code: int) -> Union["Encode", None]:
        return next((member for member in cls if member.code == code), None)

    @classmethod
    def get_by_val(cls, val: str) -> Union["Encode", None]:
        return next((member for member in cls if member.val == val), None)
