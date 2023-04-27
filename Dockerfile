FROM python:3.11-alpine3.17

RUN mkdir -p /opt/resource

RUN apk add --no-cache curl bash ca-certificates minisign bash gcompat libstdc++ libgcc && \
LATEST_VERSION=$(curl https://envkey-releases.s3.amazonaws.com/latest/cli-version.txt) && \
curl -s https://envkey-releases.s3.amazonaws.com/cli/release_artifacts/$LATEST_VERSION/install.sh | bash && \
VERSION=$(curl https://envkey-releases.s3.amazonaws.com/latest/envkeysource-version.txt) && \
curl -s https://envkey-releases.s3.amazonaws.com/envkeysource/release_artifacts/$VERSION/install.sh | bash && \
cp /usr/local/bin/envkey-source /usr/local/bin/envkey /opt/resource/ && \
apk del curl bash minisign

COPY resource /opt/resource
COPY requirements.txt /opt/resource

RUN pip install -r /opt/resource/requirements.txt