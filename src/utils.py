import pathlib

import configparser
from settings import settings


def get_bucket_objects(boto3_client, bucket_name: str):
    for key in boto3_client.list_objects(Bucket=settings.AWS_BUCKET)['Contents']:
        print(key['Key'])
    # s3.upload_file('test.txt', settings.AWS_BUCKET, 'test.txt')


def read_config() -> configparser.ConfigParser:
    home = pathlib.Path.home()
    config_path = home / ".config" / "cloudphoto" / "cloudphotorc"
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
