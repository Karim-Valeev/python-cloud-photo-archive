import os

from pydantic import BaseSettings

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION: str = os.environ.get("AWS_REGION")
    AWS_BUCKET: str = os.environ.get("AWS_BUCKET")

    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    LOGGER_NAME: str = 'app_logger'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s %(pathname)s %(lineno)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': LOG_LEVEL,
            },
        },
        'loggers': {
            'app_logger': {
                'handlers': ['console'],
                'level': LOG_LEVEL,
            },
        }
    }


settings = Settings()
