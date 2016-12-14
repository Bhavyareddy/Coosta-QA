from .base import *

DEBUG = True    # Temp setting

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coosta_db',
        'USER': 'coosta_db_user',
        'PASSWORD': 'coosta_db_pwd',
        'HOST': 'coosta-mysql',  # Set to empty string for localhost.
        'PORT': '3306',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}
