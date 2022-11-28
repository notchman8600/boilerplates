# from flask.cli import with_appcontext
from contextlib import contextmanager
from flask_sqlalchemy import SQLAlchemy
# import click


class SQLAlchemySafe(SQLAlchemy):
    """SQLAlchemy にセッション等を終了する処理を追加したラッパークラス"""

    @contextmanager
    def get_session(self):
        """withブロックでセッションを取得し、ブロックを抜けるとセッションを閉じる"""

        try:
            yield self.session

        finally:
            self.session.close()


db = SQLAlchemySafe()


def init_db(app):
    db.init_app(app)
