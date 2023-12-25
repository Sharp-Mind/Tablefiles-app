#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM python:3.10.12-alpine
WORKDIR /app/
COPY . .
# RUN apt-get update && apt-get install -y python3-pip
RUN python3 -m pip install --no-cache-dir --no-warn-script-location --upgrade pip && python3 -m pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt
