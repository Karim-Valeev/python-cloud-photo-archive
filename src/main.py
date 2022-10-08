import os
from pprint import pprint

import boto3
import requests

from config.settings import settings
from misc import s3


def get_bucket_objects(boto3_client, bucket_name: str):
    for key in boto3_client.list_objects(Bucket=settings.AWS_BUCKET)['Contents']:
        print(key['Key'])


def upload_file_to_bucket():
    pass


if __name__ == '__main__':
    print("Program started...\n")

    # get_bucket_objects(s3, settings.AWS_BUCKET)
    #
    # s3.upload_file('test.txt', settings.AWS_BUCKET, 'test.txt')
    #
    # get_bucket_objects(s3, settings.AWS_BUCKET)



    # TODO: Помотреть че такое argparse
    # TODO: Помотреть че такое configparser

    # Way of running terminal commands in python:
    # os.system("ls -a")

    # Way of making requests:
    url = f"https://functions.yandexcloud.net/d4elrmj7thsco08lickg"
    response = requests.post(
        url,
        headers={'Accept': '*/*', 'Authorization': 'Basic ...', },
        json={}
    )
    data = response.json()
    pprint(data)
