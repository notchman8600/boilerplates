# Flask(production mode) with MySQL Server

このディレクトリはFlaskを本番モードで立ち上げる構成です。
MySQLコンテナも起動しています。
WSGIサーバーにはuwsgi、Webサーバーはnginxを使っています。
デフォルトは80番でリクエストを受け付けています。
こちらのコンテナはマルチステージビルドを用いているので少しコンテナサイズが小さくなるはずです。

## How to use

Build and Run the container

```sh
docekr compose build
docker compose up -d
```

## How to test

[UI Test]
access to the http://localhost

[API Test]

```sh
curl http://localhost/api/v1/example
```

## 解説

- api.py・・・REST APIのエンドポイントを想定しています
- home.py・・・UIを表示することを想定しています
