import configparser
import pathlib

from settings import settings


def read_config() -> configparser.ConfigParser:
    home = pathlib.Path.home()
    config_path = home / '.config' / 'cloudphoto' / 'cloudphotorc'
    config = configparser.ConfigParser()
    config.read(str(config_path))
    return config


def is_configured() -> bool:
    """Проверяет, что конфигурационный файл и все необходимые опции существуют."""
    config = read_config()

    bucket = config.has_option(settings.CONFIG_DEFAULT_SECTION, 'bucket')
    aws_access_key_id = config.has_option(settings.CONFIG_DEFAULT_SECTION, 'aws_access_key_id')
    aws_secret_access_key = config.has_option(settings.CONFIG_DEFAULT_SECTION, 'aws_secret_access_key')
    endpoint_url = config.has_option(settings.CONFIG_DEFAULT_SECTION, 'endpoint_url')
    region = config.has_option(settings.CONFIG_DEFAULT_SECTION, 'region')

    return bucket and aws_access_key_id and aws_secret_access_key and endpoint_url and region


def get_album(boto3_client, bucket: str, album: str):
    """
    Возвращает список фотографий, либо, если альбом пустой, список из одного обьекта-указателя на папку альбом.
    """
    album_photos = boto3_client.list_objects(
        Bucket=bucket, Prefix=album + '/', Delimiter='/'
    ).get('Contents')
    return album_photos
