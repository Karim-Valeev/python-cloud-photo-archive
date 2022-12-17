import os

from jinja2 import Template

from templates import album_template, error_template, index_template


def mksite(boto3_client, bucket: str, *args, **kwargs):
    photos = boto3_client.list_objects(Bucket=bucket).get('Contents', [])
    if photos:
        url = f'https://{bucket}.website.yandexcloud.net/'
        albums_and_photos = {}
        for photo in photos:
            try:
                album_name, photo_name = photo['Key'].split('/')
                if not albums_and_photos.get(album_name):
                    albums_and_photos[album_name] = [photo_name]
                else:
                    albums_and_photos[album_name].append(photo_name)
            except Exception:
                pass

        albums_indexed = []
        counter = 0
        for album_name in albums_and_photos.keys():
            rendered_album_template = Template(album_template).render(
                album=album_name, photos=albums_and_photos.get(album_name), url=url
            )
            with open('tmp.html', 'w') as f:
                f.write(rendered_album_template)
            boto3_client.upload_file('tmp.html', bucket, f'album{counter}.html')
            os.remove('tmp.html')
            albums_indexed.append({
                'album_indexed_name': f'album{counter}',
                'album_name': album_name,
            })
            counter += 1

        rendered_index_template = Template(index_template).render(albums=albums_indexed)
        with open('tmp.html', 'w') as f:
            f.write(rendered_index_template)
        boto3_client.upload_file('tmp.html', bucket, 'index.html')

        with open('tmp.html', 'w') as f:
            f.write(error_template)
        boto3_client.upload_file('tmp.html', bucket, 'error.html')

        os.remove('tmp.html')

        website_configuration = {
            'ErrorDocument': {'Key': 'error.html'},
            'IndexDocument': {'Suffix': 'index.html'},
        }
        boto3_client.put_bucket_website(Bucket=bucket, WebsiteConfiguration=website_configuration)
        print(url)
    else:
        raise Exception(f'В бакете {bucket} нет фотографий')
