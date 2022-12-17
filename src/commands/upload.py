import os
from pathlib import Path

from botocore.exceptions import ClientError

from settings import settings


def make_file_cloud_name(album: str, file: str):
    return f'{album}/{file}'


def upload(boto3_client, bucket: str, args):
    path = Path(args.path)
    if not args.album:
        raise Exception('Для выгрузки фотографий необходимо ввести название альбома') from None
    if not os.path.exists(path):
        raise Exception(f'Директория {path} не найдена') from None

    uploaded_counter = 0
    for photo in path.iterdir():
        if photo.is_file() and photo.suffix in settings.FILE_EXTENSIONS:
            try:
                boto3_client.upload_file(
                    str(photo),
                    bucket,
                    make_file_cloud_name(args.album, photo.name),
                )
                uploaded_counter += 1
            except ClientError as err:
                print(err)

    if uploaded_counter == 0:
        raise Exception(
            f'В указаной директории нет файлов удволетворяющих расширениям: {settings.FILE_EXTENSIONS}'
        ) from None
