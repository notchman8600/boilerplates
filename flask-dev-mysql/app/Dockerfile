
FROM python:3.11-slim

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y pkg-config build-essential

COPY requirements.txt requirements.txt
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip pip install -r requirements.txt --no-cache-dir

EXPOSE 5000
CMD ["flask", "run"]
