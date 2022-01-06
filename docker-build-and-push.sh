#!/bin/bash
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 599087160579.dkr.ecr.ap-northeast-2.amazonaws.com
docker build -t grpc-poc ./apps
docker tag grpc-poc:latest 599087160579.dkr.ecr.ap-northeast-2.amazonaws.com/grpc-poc:latest
docker push 599087160579.dkr.ecr.ap-northeast-2.amazonaws.com/grpc-poc:latest
