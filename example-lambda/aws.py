import boto3
import json
import os
from exception import S3Exception, SecretsManagerException
from typing import Union


class S3:
    @staticmethod
    def get_object(bucket_name: str, dir: str, name: str) -> str:
        try:
            s3_client = boto3.client("s3")
            res = s3_client.get_object(Bucket=bucket_name, Key=os.path.join(dir, name))
            return res["Body"].read()
        except Exception as e:
            raise S3Exception(str(e))

    @staticmethod
    def put_object(bucket_name, dir, name, body) -> None:
        try:
            s3_client = boto3.client("s3")
            s3_client.put_object(Bucket=bucket_name, Key=os.path.join(dir, name), Body=body)
        except Exception as e:
            raise S3Exception(str(e))

    @staticmethod
    def get_key_list(bucket_name: str) -> list[str]:
        try:
            s3_client = boto3.client("s3")
            keys = []
            paginator = s3_client.get_paginator("list_objects_v2")
            for page in paginator.paginate(Bucket=bucket_name):
                if "Contents" in page:
                    for obj in page["Contents"]:
                        keys.append(obj["Key"])
            return keys
        except Exception as e:
            raise S3Exception(str(e))


class SecretsManager:
    @staticmethod
    def get_secret(secret_name: str) -> Union[dict, str]:
        try:
            client = boto3.client("secretsmanager")
            response = client.get_secret_value(SecretId=secret_name)
            if "SecretString" in response:
                secret = response["SecretString"]
                return json.loads(secret) if secret.startswith("{") else secret
            else:
                secret = response["SecretBinary"]
                return secret
        except Exception as e:
            raise SecretsManagerException(str(e))
