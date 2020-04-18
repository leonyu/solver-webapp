#!/bin/sh

gcloud functions deploy is_prime \
  --allow-unauthenticated \
  --runtime=python37 \
  --trigger-http

gcloud functions deploy solve \
  --allow-unauthenticated \
  --runtime=python37 \
  --trigger-http
