class Config(object):
    TESTING = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@mysql/sample-db"
    EXECUTOR_TYPE = 'process'
    EXECUTOR_PROPAGATE_EXCEPTIONS = True
