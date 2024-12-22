import json


class LambdaException(Exception):
    _status_code = None
    _error_msg = None

    def __init__(self, status_code: int, error_msg: str):
        self._status_code = status_code
        self._error_msg = error_msg

    def __str__(self):
        obj = {"statusCode": self._status_code, "errorMessage": self._error_msg}
        return json.dumps(obj)


class S3Exception(LambdaException):
    def __init__(self, error_msg: str):
        super().__init__(500, error_msg)


class SecretsManagerException(LambdaException):
    def __init__(self, error_msg: str):
        super().__init__(500, error_msg)


class MySqlException(LambdaException):
    def __init__(self, error_msg: str):
        super().__init__(500, error_msg)
