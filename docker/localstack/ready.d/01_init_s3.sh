#!/bin/bash

cd /etc/localstack/init/ready.d/S3

aws s3 mb s3://from-bucket
aws s3 sync ./from-bucket s3://from-bucket

aws s3 mb s3://to-bucket
aws s3 sync ./to-bucket s3://to-bucket
