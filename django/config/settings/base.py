import os
import json

# settings 파일 경로
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))

# django 프로젝트 경로
DJANGO_DIR = os.path.dirname(os.path.dirname(SETTINGS_DIR))

# 전체 프로젝트 최상단 경로
ROOT_DIR = os.path.dirname(DJANGO_DIR)

# secrets.json 설정
SECRETS_JSON_PATH = os.path.join(SETTINGS_DIR, 'secrets.json')
SECRETS_JSON = json.loads(open(SECRETS_JSON_PATH).read())

# django secret key
SECRET_KEY = SECRETS_JSON['DJANGO']['SECRET_KEY']

DEBUG = True
ALLOWED_HOSTS = []

# User model 커스텀
AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'jet.dashboard',
    'jet', # admin custom lib, before contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
]

CUSTOM_APPS = [
    'core',
    'users',
    'boards',
]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += CUSTOM_APPS

# Django REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware', # corsheaders
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# cors headers
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'config.urls'

# templates 설정
TEMPLATE_DIR = os.path.join(DJANGO_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DJANGO_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# media 설정
MEDIA_ROOT = os.path.join(DJANGO_DIR, 'media')
MEDIA_URL = '/media/'

# static 설정
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DJANGO_DIR, 'stroot')
STATIC_DIR = os.path.join(DJANGO_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
