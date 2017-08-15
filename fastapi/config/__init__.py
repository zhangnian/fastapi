from .dev import DevConfig
from .test import TestConfig
from .prod import ProdConfig


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}