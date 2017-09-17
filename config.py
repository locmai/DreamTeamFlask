# Enable Flask's debugging mode


class Config(object):
    DEBUG = True


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
