from aws import S3
from mysql_dao import UserDao
from enums import Encode


def lambda_handler():
    results = UserDao().find()
    for ret in results:
        print(ret)

    result = UserDao().find_by_id(1)
    print(result)

    bucket_name = "from-bucket"
    keys = S3.get_key_list(bucket_name)
    for key in keys:
        print(key)

    file_content = S3.get_object(bucket_name, "", "hoge.txt")
    decoded_file_content = file_content.decode("utf-8")
    print(decoded_file_content)

    S3.put_object(bucket_name, "", "fuga.txt", decoded_file_content)

    print(Encode.get_by_id(1))
    print(Encode.get_by_val("UTF-8"))


lambda_handler()
