from .default import Config

class ProdConfig(Config):
    LOG_LEVEL = 'error'