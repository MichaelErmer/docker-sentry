# This file is just Python, with a touch of Django which means you
# you can inherit and tweak settings to your hearts content.
from sentry.conf.server import *
import os

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

CONF_ROOT = os.path.dirname(__file__)
TIME_ZONE = 'Europe/Oslo'

# Remeber to set the SECRET_KEY environment variable when putting this into
# production so no one can spoofe your sessions. Changing this will cause your
# current user sessions to become invalidated.
SECRET_KEY = os.environ.get('SECRET_KEY') or 'notasecret'

# This is only acceptable if we are behind some kind of reverse proxy, or a HTTP
# load ballancer, since it will do the HOST name checking for us!
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',

        # If you're using Postgres, we recommend turning on autocommit
        'OPTIONS': {
            'autocommit': True,
        },
    }
}


SENTRY_REDIS_OPTIONS = {
    'hosts': {
        0: {
            'host': 'redis',
            'port': 6379,
            'db': 0
        },
    }   
}   

SENTRY_TSDB = 'sentry.tsdb.redis.RedisTSDB'
SENTRY_TSDB_OPTIONS = {
    'hosts': {
        0: {
            'host': 'redis',
            'port': 6379,
            'db': 1
        }
    }
}

 
SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
SENTRY_BUFFER_OPTIONS = {
    'hosts': {
        0: {
            'host': 'redis',
            'port': 6379,
            'db': 2
        }
    }
}

 
BROKER_URL = "redis://redis:6379/3"

SENTRY_CACHE = 'sentry.cache.redis.RedisCache'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHE_VERSION = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', ''))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = str2bool(os.environ.get('EMAIL_USE_TLS', "True"))

# The email address to send on behalf of
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX') or 'http://example.com'
SERVER_EMAIL = os.environ.get('SERVER_EMAIL') or 'root@localhost'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 8080
SENTRY_WEB_OPTIONS = {
    'workers': 3,             # number of gunicorn workers
    'limit_request_line': 0,  # required for raven-js
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

# If you're using a reverse proxy, you should enable the X-Forwarded-Proto
# and X-Forwarded-Host headers, and uncomment the following settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

SENTRY_FEATURES['auth:register'] = str2bool(os.environ.get('ALLOW_REGISTRATION', "False"))
SENTRY_FEATURES['organizations:sso'] = str2bool(os.environ.get('ALLOW_SSO', "False"))