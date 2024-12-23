from aws import S3
from mysql_dao import UserDao
from enums import Encoding, UserType


def lambda_handler():
    results = UserDao().sql_find_all()
    for ret in results:
        print(ret)

    result = UserDao().sql_find_by_id(1)
    print(result)

    results = UserDao().find_all()
    for ret in results:
        print(ret.last_name)

    result = UserDao().find_by_type(UserType.PRIVATE)
    print(result.last_name)

    bucket_name = "from-bucket"
    keys = S3.get_key_list(bucket_name)
    for key in keys:
        print(key)

    file_content = S3.get_object(bucket_name, "", "hoge.txt")
    decoded_file_content = file_content.decode("utf-8")
    print(decoded_file_content)

    S3.put_object(bucket_name, "", "fuga.txt", decoded_file_content)

    print(Encoding.get_by_id(1))
    print(Encoding.get_by_val("UTF-8"))


lambda_handler()
