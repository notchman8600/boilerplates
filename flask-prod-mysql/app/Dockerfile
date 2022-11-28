FROM python:3.11-bullseye as builder

RUN apt update && apt upgrade -y && apt install -y gcc g++ build-essential pkg-config
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

FROM python:3.11-slim

ARG FLASK_DEBUG="false"
WORKDIR /usr/src/app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

RUN apt update \
  && apt install -y libpq5 libxml2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \

ENV FLASK_DEBUG="${FLASK_DEBUG}" \
FLASK_SKIP_DOTENV="true" \
PYTHONUNBUFFERED="true" \
PYTHONPATH="." \
PATH="${PATH}:/home/python/.local/bin" \
USER="python"

COPY . .

EXPOSE 5000
WORKDIR /usr/src/app

CMD ["uwsgi", "--ini", "sample_app/app.ini","--enable-threads"]
