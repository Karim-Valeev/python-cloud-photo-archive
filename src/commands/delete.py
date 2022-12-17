from botocore.exceptions import ClientError

from utils import get_album


def delete(boto3_client, bucket: str, args):
    if not args.album:
        raise Exception('Для удаления фотографий необходимо ввести название альбома') from None

    album = get_album(boto3_client, bucket, args.album)
    if album:
        photo_name = args.photo
        if photo_name:
            photo_path = f'{args.album}/{photo_name}'
            try:
                boto3_client.get_object(Bucket=bucket, Key=photo_path)
            except ClientError as err:
                if err.response['Error']['Code'] == 'NoSuchKey':
                    raise Exception(f'Такой фотографии в альбоме {args.album} не существует') from None
            photo_keys = [{'Key': photo_path}]
        else:
            photo_keys = [{'Key': photo['Key']} for photo in album]
        boto3_client.delete_objects(
            Bucket=bucket, Delete={'Objects': photo_keys}
        )
    else:
        raise Exception(f'Альбома {args.album} не сущетсвует.') from None
