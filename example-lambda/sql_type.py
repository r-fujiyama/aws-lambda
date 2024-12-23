from sqlalchemy import Integer

# from enums import ABCEnumMeta
from sqlalchemy.types import TypeDecorator


class IntEnum(TypeDecorator):
    impl = Integer
    cache_ok = True

    def __init__(self, enum_class, *args, **kwargs):
        self.enum_class = enum_class
        super().__init__(*args, **kwargs)

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not isinstance(value, self.enum_class):
                raise TypeError("Value should be an instance of %s" % self.enum_class)
            return value.code

    def process_result_value(self, value, dialect):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("value should have int type")
            return self.enum_class.get_by_id(value)
