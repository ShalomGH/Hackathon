"""
Django settings for StartUpHackaton project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import logging
import os
from pathlib import Path


from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Connecting environment variables or create .env file if it doesn't exist
dotenv_path = os.path.join(BASE_DIR, '.env')

if not os.getenv('ACTIONS'):
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        with open('.env', 'w') as env:
            env.write('GROUP_API_KEY=\n'
                      'DATABASE_NAME=\n'
                      'DATABASE_USER=\n'
                      'DATABASE_PASSWORD=\n'
                      'DATABASE_HOST=\n'
                      'DATABASE_PORT=\n'
                      'SECRET_KEY=\n'
                      'EMAIL_HOST_USER=\n'
                      'EMAIL_HOST_PASSWORD=\n'
                      'EMAIL_HOST=\n'
                      'EMAIL_PORT='
                      )
        raise Exception('You need to fill in the .env file')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users_app',

    'users_app.usersAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StartUpHackaton.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'StartUpHackaton.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING_SETTINGS = {
    'DATEFORMAT': '%d-%m-%Y %H:%M:%S',
    'FORMAT': '[{asctime}] [{levelname:>7}] [{name}] :: {message}',
    'CONSOLE_LEVEL': logging.DEBUG,
    'DJANGO_CONSOLE_LEVEL': logging.INFO,
    'FILE_LEVEL': logging.INFO,
    'FILENAME': 'project.log',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'create_model_color': {
            '()': 'StartUpHackaton.logger.CreationFormatter',
        },
        'color_verbose': {
            '()': 'StartUpHackaton.logger.CustomFormatter',
            'colored': True
        },
        'colorless_verbose': {
            '()': 'StartUpHackaton.logger.CustomFormatter',
            'colored': False
        },
    },
    'filters': {
        'without_get': {
            '()': 'StartUpHackaton.logger.SkipStaticFilter'
        }
    },
    'handlers': {
        'console': {
            'level': LOGGING_SETTINGS['CONSOLE_LEVEL'],
            'filters': ['without_get'],
            'class': 'logging.StreamHandler',
            'formatter': 'color_verbose'
        },
        'create_model': {
            'level': LOGGING_SETTINGS['CONSOLE_LEVEL'],
            'filters': ['without_get'],
            'class': 'logging.StreamHandler',
            'formatter': 'create_model_color'
        },
        'file': {
            'level': LOGGING_SETTINGS['FILE_LEVEL'],
            'filters': ['without_get'],
            'formatter': 'colorless_verbose',
            'class': 'logging.FileHandler',
            'filename': 'project.log',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'propagate': False,
            'level': LOGGING_SETTINGS['DJANGO_CONSOLE_LEVEL'],
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': LOGGING_SETTINGS['DJANGO_CONSOLE_LEVEL'],
            'propagate': False,
        },
        'users_app.managers': {
            'handlers': ['create_model', 'file'],
            'level': LOGGING_SETTINGS['DJANGO_CONSOLE_LEVEL'],
            'propagate': False,
        },
        'companies_app.managers': {
            'handlers': ['create_model', 'file'],
            'level': LOGGING_SETTINGS['DJANGO_CONSOLE_LEVEL'],
            'propagate': False,
        },
        'cars_app.managers': {
            'handlers': ['create_model', 'file'],
            'level': LOGGING_SETTINGS['DJANGO_CONSOLE_LEVEL'],
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': LOGGING_SETTINGS['CONSOLE_LEVEL'],
        }
    }
}

AUTH_USER_MODEL = 'users_app.User'
AUTHENTICATION_BACKENDS = ('users_app.backends.AuthBackend',)

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': 'Bearer'
}


DJOSER_SERIALIZERS = {
    'user_create_password_retype': 'users_app.serializers.UserSerializer',
}


# Djoser settings
DJOSER = {
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SEND_ACTIVATION_EMAIL': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'TOKEN_MODEL': None,  # only JWT
    'ACTIVATION_URL': 'api/v1/users/email/activate/{uid}/{token}',
    'SERIALIZERS': DJOSER_SERIALIZERS,
}


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
