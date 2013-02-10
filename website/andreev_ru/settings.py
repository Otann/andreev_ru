# coding=utf-8
import os
import socket

DEV_MODE = 'nest-frontend' != socket.gethostname() and 'pavel-andreev.ru' != socket.gethostname()
if DEV_MODE:
    DEBUG = True
    from settings_dev import *
else:
    DEBUG = False
    from settings_prod import *

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Anton Chebotaev', 'anton.chebotaev@gmail.com'),
    ('Artur Paikin', 'arturpaikin@arturpaikin.com'),
    )

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
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
    # Before using site cache consider amount of quick searches and how fast they will stale cache
    # 'django.middleware.cache.UpdateCacheMiddleware',  # This should be first allways

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'andreev_ru.main.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',  # This should be last allways
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
        'forcePasteAsPlainText': True,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            {
                'name': 'main',
                'items': [
                    'Bold','Italic','Underline','Strike','Subscript','Superscript',
                    'Link', 'Unlink','RemoveFormat','-',
                    'NumberedList', 'BulletedList','Blockquote','-',
                    'Maximize',
                    'ImageButton'
                    # 'Find','Replace'
                ]
            }
        ],
    },
}

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = ('image_cropping.thumbnail_processors.crop_corners',) + thumbnail_settings.THUMBNAIL_PROCESSORS
IMAGE_CROPPING_THUMB_SIZE = (300, 300)

INSTALLED_APPS = (

    'grappelli.dashboard',
    'andreev_ru.main',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.admindocs',


    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Mosels synching applications
    'south',

    # Multilingual models app
    'modeltranslation',

    # CKEditor for WYSIWYG
    'ckeditor',

    # thumbnails
    'easy_thumbnails',
    'image_cropping',
    )


