import os
from pathlib import Path


def get_album_photos(boto3_client, bucket: str, album: str):
    album_photos = boto3_client.list_objects(
        Bucket=bucket, Prefix=album + "/", Delimiter="/"
    ).get('Contents')
    return album_photos


def download(boto3_client, bucket: str, args):
    path = Path(args.path)
    if not args.album:
        raise Exception(f'Для загрузки фотографий необходимо ввести название альбома') from None
    if not os.path.exists(path):
        raise Exception(f'Директория {path} не найдена') from None

    album_photos = get_album_photos(boto3_client, bucket, args.album)
    if album_photos:
        for photo in album_photos:
            response = boto3_client.get_object(Bucket=bucket, Key=photo["Key"])
            filename = photo["Key"].split("/")[1]
            filepath = path / filename
            with filepath.open("wb") as f:
                f.write(response["Body"].read())
    else:
        raise Exception(f'Альбома {args.album} не сущетсвует.') from None

