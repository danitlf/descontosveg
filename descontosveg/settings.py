import os
from unipath import Path
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api




PROJECT_DIR = Path(__file__).parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'descontosveg@gmail.com'
EMAIL_HOST_PASSWORD = 'gestao2017'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '30b8jzx2hq_5y+mqs=cyq*b_r+ii2-=01-34s_u_w2!5se_k(3'




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.localhost', '127.0.0.1', '.herokuapp.com', '.vegdescontos.com.br'
    ]


# Application definition

INSTALLED_APPS = [
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'descontosveg.book',
    'descontosveg.moip',
    'storages',
    
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'descontosveg.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'descontosveg.wsgi.application'






# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
   'default': dj_database_url.config(
       default = 'sqlite:///' + PROJECT_DIR.child('database.db'))
   
}



ADMIN_SITE_HEADER = "DescontosVEG | Admin"

##
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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



# ESQUEMA DE LOGIN
AUTH_PROFILE_MODULE = 'admin'

LOGIN_URL = 'django.contrib.auth.views.login'

LOGIN_REDIRECT_URL  =  '/'

LOGOUT_REDIRECT_URL  =  '/'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'



STATIC_ROOT = PROJECT_DIR.child('staticfiles',)


AWS_S3_HOST ="s3-sa-east-1.amazonaws.com"

AWS_QUERYSTRING_AUTH = False

AWS_ACCESS_KEY_ID = 'AKIAIN663JY4VBCHWZBA'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'descontosveg'

MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"



# AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'Cache-Control': 'max-age=94608000',
# }

# AWS_STORAGE_BUCKET_NAME = 'vegdescontos'
# AWS_ACCESS_KEY_ID = 'AKIAIB3MQJ2FOH33GERA'
# AWS_SECRET_ACCESS_KEY = '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'


# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MOIP_PROD = True


