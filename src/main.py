import argparse
# TODO: Разкомментить
# import sys
from commands import delete, download, init, list, mksite, upload

import boto3

from settings import settings
from utils import is_configured, read_config

COMMANDS = {
    'delete': delete,
    'download': download,
    'init': init,
    'list': list,
    'mksite': mksite,
    'upload': upload,
}


def main():
    # TODO: Разкомментить
    # sys.tracebacklimit = -1

    parser = argparse.ArgumentParser(description='Python cloud photo archive with Yandex Cloud.')
    parser.add_argument('app')
    parser.add_argument('command')
    parser.add_argument('--album', default=None)
    parser.add_argument('--photo', default=None)
    parser.add_argument('--path', default='.')
    args = parser.parse_args()

    if args.app == settings.APP_NAME:
        try:
            command_name = args.command
            command = COMMANDS[command_name]
        except KeyError:
            raise Exception(f'Введите команду из списка доступных: {[COMMANDS.keys()]}') from None
    else:
        raise Exception(f'Неправильное название приложения. Доступные: {settings.APP_NAME}') from None

    if command_name == 'init':
        command()
    else:
        configured = is_configured()
        if configured:
            config = read_config()
            session = boto3.session.Session()
            boto3_client = session.client(
                service_name=settings.SERVICE_NAME,
                endpoint_url=config.get(settings.CONFIG_DEFAULT_SECTION, 'endpoint_url'),
                aws_access_key_id=config.get(settings.CONFIG_DEFAULT_SECTION, 'aws_access_key_id'),
                aws_secret_access_key=config.get(settings.CONFIG_DEFAULT_SECTION, 'aws_secret_access_key'),
                region_name=config.get(settings.CONFIG_DEFAULT_SECTION, 'region'),
            )
            bucket = config.get(settings.CONFIG_DEFAULT_SECTION, 'bucket')
            command(boto3_client, bucket, args)
        else:
            raise Exception('Выполните команду init') from None


if __name__ == '__main__':
    main()
