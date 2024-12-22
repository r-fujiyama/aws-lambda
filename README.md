# 準備

1. LocalStackの初期化シェルに実行権限を付与する。
    ```shell
    find ./docker/localstack/ready.d/ -type f -name "*.sh" -exec chmod +x {} \;
    ```

# AWSコマンド

## S3

```shell
aws s3 mb s3://from-bucket
aws s3 ls
aws s3 sync ./docker/localstack/ready.d/S3/from-bucket s3://from-bucket
aws s3 ls s3://from-bucket
```

## SecretsManager

```shell
aws secretsmanager create-secret \
    --name mysql-secrets \
    --secret-string file://./docker/localstack/ready.d/SecretsManager/mysql-secrets.json
aws secretsmanager list-secrets
aws secretsmanager get-secret-value --secret-id mysql-secrets
```
