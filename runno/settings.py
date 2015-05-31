"""
Django settings for runno project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

#if socket.gethostname() == 'Crayons-MacBook-Pro.local':
#    DEBUG = TEMPLATE_DEBUG = True
#else:
DEBUG = TEMPLATE_DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR,'templates'),
        )

STATICFILES_DIRS = (
        os.path.join(BASE_DIR,'static/'),
        'runno/static/unno'
        )

#STATICFILES_FINDERS = (
#        'django.contrib.staticfiles.finders.FileSystemFinder',
#        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#        'django.contrib.staticfiles.finders.DefaultStorageFinder',
#        )

STATIC_URL = '/static/'
#STATIC_ROOT = '/Users/Crayon_277/Develop/Project/Django/runno/static'
#SITES = {
#        1:{"domain":"localhost:8000","scheme":"http"},
#        2:{"domain":"crayon-chaney.com",'scheme':'http'},
#}

SITE_ID = 1

#SITE_ID = 2
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2u3q-z9tc+yjq*9i9wjs0b^wyr3bdrxne5u9!iy=b4+s92wq0'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'markup_deprecated',
    'django.contrib.comments',
    'django.contrib.sites',
    'unno',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.locale.Localemiddleware',
)

ROOT_URLCONF = 'runno.urls'

WSGI_APPLICATION = 'runno.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'unno/db.sqlite3'),
        'USER':'chenye277',
        'PASSWORD':'Chenye201',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

