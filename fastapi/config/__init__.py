import os


def load_config():
    """加载配置类"""
    run_mode = os.environ.get('RUN_MODE', 'DEV')
    try:
        if run_mode == 'DEV':
            from .dev import DevConfig
            return DevConfig
        elif run_mode == 'PRODUCTION':
            from .prod import ProdConfig
            return ProdConfig
        else:
            from .dev import DevConfig
            return DevConfig
    except ImportError:
        from .dev import DevConfig
        return DevConfig