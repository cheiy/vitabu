# config.py

class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    TESTING = True


app_config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
        }
