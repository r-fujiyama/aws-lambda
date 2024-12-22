from sqlalchemy import create_engine, text, TextClause
from aws import SecretsManager
from exception import MySqlException
from const import MYSQL_SECRETS_NAME
import inspect
import os

_CONN = None
_BASE_DIR = "sql/mysql"


class _Dao:
    def __init__(self):
        global _CONN
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
            except Exception as e:
                raise MySqlException(str(e))

    def _get_query(self) -> TextClause:
        func_name = inspect.stack()[1].function
        class_name = self.__class__.__name__
        path = os.path.join(_BASE_DIR, class_name, func_name + ".sql")
        f = open(path, "r", newline="\n", encoding="UTF-8")
        return text(f.read())


class UserDao(_Dao):
    def find(self) -> list[dict]:
        return _CONN.execute(self._get_query()).mappings().all()

    def find_by_id(self, id: int) -> dict:
        params = {"id": id}
        ret = _CONN.execute(self._get_query(), params).mappings().all()
        return ret[0] if ret else {}
