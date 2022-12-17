from utils import get_album


def list(boto3_client, bucket: str, args):
    if not args.album:
        album_names = set()
        photos = boto3_client.list_objects(Bucket=bucket).get('Contents', [])
        for photo in photos:
            album_names.add(photo['Key'].split('/')[0])

        if album_names:
            for name in album_names:
                print(name)
        else:
            raise Exception(f'В бакете {bucket} нет альбомов') from None
    else:
        album = get_album(boto3_client, bucket, args.album)
        if album:
            if album[0]['Key'] == args.album + '/':
                raise Exception(f'Альбом {args.album} пустой') from None
            else:
                for photo in album:
                    photo_name = photo['Key'].split('/')[1]
                    print(photo_name)
        else:
            raise Exception(f'Альбома {args.album} не сущетсвует.') from None
