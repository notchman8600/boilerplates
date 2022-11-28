# Flask(develop mode) with MySQL Server

このディレクトリはFlaskを開発者モードで立ち上げる構成です。
MySQLコンテナも起動しています。

## How to use

Build and Run the container

```sh
docekr compose build
docker compose up -d
```

## How to test

[UI Test]
access to the http://localhost:5001

[API Test]

```sh
curl http://localhost:5001/api/v1/example
```

## 解説

- api.py・・・REST APIのエンドポイントを想定しています
- home.py・・・UIを表示することを想定しています