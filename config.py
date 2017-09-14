#Enable Flask's debugging mode

class Config(object):
    pass
   #radnom

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class ProductionConfig(Config):
    DEBUG = False

app_config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}
