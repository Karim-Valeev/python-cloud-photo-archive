import sys

from commands.init import init
from commands.list import list
from config.settings import settings
from utils import is_configured

COMMANDS = {
    'init': init,
    'list': list,
}


def main():
    # TODO: Разкомментить
    # sys.tracebacklimit = -1
    try:
        app_name = sys.argv[1]
    except Exception:
        raise Exception("Введите название вызываемого приложения и команду")

    if app_name == settings.APP_NAME:
        try:
            command_name= sys.argv[2]
            command = COMMANDS[command_name]
        except Exception:
            raise Exception(f'Введите команду из списка доступных: {[COMMANDS.keys()]}')
    else:
        raise Exception(f"Неправильное название приложения. Доступное: {settings.APP_NAME}")

    if command_name == 'init':
        command()
    else:
        configured = is_configured()
        if configured:
            pass
        else:
            raise Exception('Выполните команду init')


if __name__ == '__main__':
    main()
