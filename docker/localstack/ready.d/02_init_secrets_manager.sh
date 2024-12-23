#!/bin/bash

cd /etc/localstack/init/ready.d/SecretsManager

aws secretsmanager create-secret \
    --name mysql-secrets \
    --secret-string file://./mysql-secrets.json
