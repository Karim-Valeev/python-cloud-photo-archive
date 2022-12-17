import pathlib

import configparser

import boto3
from botocore.exceptions import ClientError

from settings import settings


def init():
    """
    После запроса параметров у пользователя в интерактивном режиме записывает их в конфигурационный файд.
    Создает бакет с именем, указанном в конфигурационном файле, если такого не существует.
    """
    aws_access_key_id = input("aws_access_key_id: ")
    aws_secret_access_key = input("aws_secret_access_key: ")
    bucket = input("bucket: ")

    try:
        session = boto3.session.Session()
        s3 = session.client(
            service_name=settings.SERVICE_NAME,
            endpoint_url=settings.ENDPOINT_URL,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=settings.AWS_REGION,
        )
        s3.create_bucket(Bucket=bucket, ACL='public-read-write')
    except ClientError as err:
        if err.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            pass
        else:
            raise err

    home = pathlib.Path.home()
    config_path = home / ".config" / "cloudphoto"
    config_path.mkdir(parents=True, exist_ok=True)
    config_path /= "cloudphotorc"
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'bucket': bucket,
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key,
        'endpoint_url': settings.ENDPOINT_URL,
        'region': settings.AWS_REGION,
    }
    with open(config_path, 'w') as f:
        config.write(f)
