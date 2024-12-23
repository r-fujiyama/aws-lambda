from sqlalchemy import create_engine, text, TextClause
from sqlalchemy.orm import sessionmaker
from aws import SecretsManager
from exception import MySqlException
from const import MYSQL_SECRETS_NAME
import inspect
import os
from enums import Encoding, NewLine, UserType
from mysql_eneity import User

_CONN = None
_SESSION = None
_BASE_DIR = "sql/mysql"


class _Dao:
    def __init__(self):
        global _CONN, _SESSION
        if _CONN is None:
            mysql_secret = SecretsManager.get_secret(MYSQL_SECRETS_NAME)
            db_url = (
                f"{mysql_secret['engine']}+pymysql://"
                f"{mysql_secret['username']}:{mysql_secret['password']}@"
                f"{mysql_secret['host']}:{mysql_secret['port']}/{mysql_secret['dbname']}"
            )
            engine = create_engine(db_url)
            try:
                _CONN = engine.connect()
                _SESSION = sessionmaker(engine)()
            except Exception as e:
                raise MySqlException(str(e))

    def _get_query(self) -> TextClause:
        func_name = inspect.stack()[1].function
        class_name = self.__class__.__name__
        path = os.path.join(_BASE_DIR, class_name, func_name + ".sql")
        f = open(path, "r", newline=NewLine.LF.val, encoding=Encoding.UTF_8.val)
        return text(f.read())


class UserDao(_Dao):
    def sql_find_all(self) -> list[dict]:
        return _CONN.execute(self._get_query()).mappings().all()

    def sql_find_by_id(self, id: int) -> dict:
        params = {"id": id}
        ret = _CONN.execute(self._get_query(), params).mappings().all()
        return ret[0] if ret else {}

    def find_all(self) -> list[User]:
        return _SESSION.query(User).all()

    def find_by_type(self, type: UserType) -> User:
        return _SESSION.query(User).filter(User.type == type).one()
