import os
from pathlib import Path

from utils import get_album


def download(boto3_client, bucket: str, args):
    path = Path(args.path)
    if not args.album:
        raise Exception(f'Для загрузки фотографий необходимо ввести название альбома') from None
    if not os.path.exists(path):
        raise Exception(f'Директория {path} не найдена') from None

    album = get_album(boto3_client, bucket, args.album)
    if album:
        if album[0]["Key"] == args.album + '/':
            print(f'Альбом {args.album} пустой')
        else:
            for photo in album:
                print(photo)
                response = boto3_client.get_object(Bucket=bucket, Key=photo["Key"])
                filename = photo["Key"].split("/")[1]
                filepath = path / filename
                with filepath.open("wb") as f:
                    f.write(response["Body"].read())
    else:
        raise Exception(f'Альбома {args.album} не сущетсвует.') from None

