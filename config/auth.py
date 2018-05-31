from . import env

DEFAULT_LOGIN = env.get('DEFAULT_LOGIN')
DEFAULT_PASSWORD = env.get('DEFAULT_PASSWORD')

if not (DEFAULT_PASSWORD and DEFAULT_LOGIN):
    raise ValueError('Login and password are not defined')

USERS = {
    'default': {
        'password': DEFAULT_PASSWORD,
        'email': DEFAULT_LOGIN,
    },
}


def get_user(user):
    _user = USERS.get(user)
    if not _user:
        raise ValueError('Undefined user name')
    return _user
