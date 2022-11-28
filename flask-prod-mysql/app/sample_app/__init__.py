import os
from flask import Flask
from flask_migrate import Migrate
from .config import ProductionConfig
from .database import db


def create_app():
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True)

    with app.app_context():

        app.config.from_object(ProductionConfig)

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        db.init_app(app)
        db.create_all()
        _migrate = Migrate(app, db, compare_type=True)
        _migrate.init_app(app, db)
        app.db = db

        from . import home
        app.register_blueprint(home.bp)
        
        from . import api
        app.register_blueprint(api.bp)

    return app
