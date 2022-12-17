from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'cloudphoto'
    SERVICE_NAME: str = 's3'
    ENDPOINT_URL: str = 'https://storage.yandexcloud.net'
    AWS_REGION: str = 'ru-central1'
    CONFIG_DEFAULT_SECTION: str = 'DEFAULT'
    FILE_EXTENSIONS = ['.jpg', '.jpeg']


settings = Settings()
