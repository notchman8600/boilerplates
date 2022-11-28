class Config(object):
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@mysql/sample-db"

