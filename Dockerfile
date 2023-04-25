FROM python:3.11-alpine3.17

RUN apk add --no-cache curl bash ca-certificates && \
  VERSION=$(curl https://envkey-releases.s3.amazonaws.com/latest/envkeysource-version.txt) && \
  curl -s https://envkey-releases.s3.amazonaws.com/envkeysource/release_artifacts/$VERSION/install.sh | bash && \
  apk del curl bash

RUN mkdir -p /opt/resource

COPY resource /opt/resource
COPY requirements.txt /opt/resource

RUN pip install -r /opt/resource/requirements.txt