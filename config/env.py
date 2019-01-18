import os


def get(key, default=None):
    return os.environ.get(key=key, default=default)


def get_bool(key, default=None):
    value = get(key, default)
    return f'{value}'.lower() == 'true'
