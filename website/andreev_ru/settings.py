# coding=utf-8
import os
import socket

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Anton Chebotaev', 'anton.chebotaev@gmail.com'),
    ('Artur Paikin', 'arturpaikin@arturpaikin.com'),
    )

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'andreev_ru',                 # Or path to database file if using sqlite3.
        'USER': 'root',                       # Not used with sqlite3.
        'PASSWORD': 'password',               # Not used with sqlite3.
        'HOST': 'localhost',                  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
           "init_command": "SET storage_engine=MyISAM", # for fulltext search
        }
    }
}

if 'nest-frontend' != socket.gethostname():
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local-database',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
#STORAGE_ROOT = os.path.join('/static', PROJECT_NAME)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media') #todo(Anton) replace with STORAGE_ROOT
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static') #todo(Anton) replace with STORAGE_ROOT
STATIC_URL = '/static/'

# Settings for django-modeltranslation
gettext = lambda s: s
LANGUAGES = (
    ('ru', u'Русский'),
    ('en', u'English'),
    )
LANGUAGE_CODE = 'ru'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'andreev_ru.translation'

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'ckeditor')


STATICFILES_DIRS = ( )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'hu-5%d%9-(kc&amp;yi_fs$zv_2*!de@-youcrzkpaovx_t4exndqz'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'andreev_ru.main.context_processors.pages_processor'
    )

ROOT_URLCONF = 'andreev_ru.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'andreev_ru.wsgi.application'

TEMPLATE_DIRS = ( )

GRAPPELLI_INDEX_DASHBOARD = 'andreev_ru.dashboard.CustomIndexDashboard'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'forcePasteAsPlainText': True,
    },
}

INSTALLED_APPS = (

    'grappelli.dashboard',
    'grappelli',
    'andreev_ru.main',

    'django.contrib.admin',
    'django.contrib.admindocs',


    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django.contrib.sites',
#    'django.contrib.flatpages',

    # Mosels synching applications
    'south',

    # Multilingual models app
    'modeltranslation',

    # CKEditor for WYSIWYG
    'ckeditor',
    )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

