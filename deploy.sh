#!/bin/bash

set -e

APP_NAME='solver-webapp'

BRANCH_NAME="$(git rev-parse --abbrev-ref HEAD)"
REPOSITORY_JSON=$(aws ecr describe-repositories --repository-names $APP_NAME --output json)
REPOSITORY_URI=$(echo "$REPOSITORY_JSON" | python3 -c 'import json, sys; print(json.load(sys.stdin)["repositories"][0]["repositoryUri"])')

if [ "$BRANCH_NAME" == 'HEAD' ]; then
    echo 'Not on a git branch'
    exit 1
elif [ "$BRANCH_NAME" == 'master' ]; then
    TAG=latest
else
    TAG="$BRANCH_NAME"
fi

echo -e "Building Docker image and deploying to '$REPOSITORY_URI:$TAG'\n"

docker build -t "$APP_NAME:$TAG" .
docker tag "$APP_NAME:$TAG" "$REPOSITORY_URI:$TAG"
ECR_LOGIN="$(aws ecr get-login --no-include-email --region us-east-1)"
${ECR_LOGIN}
sleep 1
docker push "$REPOSITORY_URI:$TAG"
