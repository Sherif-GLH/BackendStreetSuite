"""
Django settings for Streetsuite project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta
from celery.schedules import crontab

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ze!xanmdw6x-z25g9sye)0=v!5j2&(^otowa24-u^_1)3b*lti'

# SECURITY WARNING: don't run with debug turned on in production!
 
DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1',
#                  'abdulrahman.onrender.com',
#                  'localhost:8000',
#                  'localhost:3000',              
# ]

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'daphne',
    'Alerts',
    'UserApp',
    'BlogApp',
    'Payment',
    "reviewapp",
    'QuizApp',
    'vacancies',
    'contactus',
    'change_log',
    'Courses',
    'leaderboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_yasg',
    'django.contrib.sites',
    'stripe',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'corsheaders',
    'channels',
    'storages',
    'rest_framework_simplejwt',  
    # 'rest_framework_simplejwt.token_blacklist',  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [ 'http://localhost:3000', 'http://127.0.0.1:3000', 'https://abdulrahman.onrender.com', 'http://localhost:8000', 'http://127.0.0.1:8000' ]

ROOT_URLCONF = 'Streetsuite.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# WSGI_APPLICATION = 'Streetsuite.wsgi.application'

ASGI_APPLICATION = 'Streetsuite.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }


USE_TZ = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.getenv("DB_NAME"),
#         'USER': os.getenv("DB_USER"),
#         'PASSWORD': os.getenv("DB_PASS"),
#         'HOST': os.getenv("DB_HOST"),  
#         'PORT': os.getenv("DB_PORT"),  
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'streetsuite_db',
        'USER': 'StreetSuite',
        'PASSWORD': 'StreetSuite123456',
        'HOST': 'streetsuitedb.cf44wuiog9cc.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# MEDIA_URL = "Media/"
# MEDIA_ROOT =  BASE_DIR / "Media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        
}
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    },
}
AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    
]
######## JWT ########
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,            
    'AUTH_HEADER_TYPES': ('Token',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'TOKEN_TYPE_CLAIM': 'Token',
    "TOKEN_OBTAIN_SERIALIZER": "UserApp.api.serializers.CustomTokenObtainPairSerializer",
}
#######################

# Google Configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("GOOGLE_OAUTH2_SECRET")

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_ID = 1
LOGIN_REDIRECT_URL = '/blogs/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'


STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_WEBHOOK_KEY = os.getenv('STRIPE_WEBHOOK_KEY')


#### for gmail verification ####
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # Port for SMTP
EMAIL_USE_TLS = True  # Transport Layer Security is required by Gmail
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER") # Your Gmail address
EMAIL_FROM = os.getenv("EMAIL_FROM")  # Your Gmail address
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")  # Your Gmail password or app-specific password
# DEFAULT_FROM_EMAIL = 'streetsuits@gmail.com'  # Default sender email address
PASSWORD_RESET_TIMEOUT = 14400

## celery conf ##
## celery configuration settings ##
CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORTS = ('Alerts.tasks',)
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'tasks-1-day': {
        'task': 'Alerts.tasks.tasks_1day',
        'schedule': crontab(minute=40, hour=12),
        # "schedule":10 
    },
    'tasks-1-hour': {
        'task': 'Alerts.tasks.tasks_1hour',
        'schedule': crontab(minute=0,hour='*/1'),
        # "schedule":10 
    },
    'tasks-4-hour': {
        'task': 'Alerts.tasks.tasks_4hour',
        'schedule': crontab(minute=0,hour='*/4'),
        # "schedule":10 
    },
    # 'rsi-every-1-day': {
    #     'task': 'Alerts.tasks.RSI_1day',
    #     'schedule': crontab(minute=0, hour=16),
    #     # "schedule":10 
    # },
    # 'rsi-every-4-hours': {
    #     'task': 'Alerts.tasks.RSI_4hour',
    #     'schedule': crontab(minute=0, hour='*/4'),
    #     # "schedule":60
    # },
    # 'ema-every-1-day': {
    #     'task': 'Alerts.tasks.EMA_DAY',
    #     'schedule': crontab(minute=0, hour=16),
    #     # "schedule":10 
    # },
    # 'ema-every-4-hours': {
    #     'task': 'Alerts.tasks.EMA_4HOUR',
    #     'schedule': crontab(minute=0, hour='*/4'),
    #     # "schedule":20 
    # },
    # 'ema-every-1-hour': {
    #     'task': 'Alerts.tasks.EMA_1HOUR',
    #     'schedule': crontab(minute=0, hour='*/1'),
    #     # "schedule":30 
    # },
    'webscraper': 
    {
        'task': 'Alerts.tasks.twitter_scrap',
        'schedule': crontab(minute=36, hour=14, day_of_month=22),
        # "schedule":20 
    },
    # 'Earning-15-days': {
    #     'task': 'Alerts.tasks.earning15',
    #     'schedule': crontab(minute='*/3'),
    #     # 'schedule': crontab(minute=42, hour=6),
    #     # "schedule":10 
    # },
    # 'Earning-30-days': {
    #     'task': 'Alerts.tasks.earning30',
    #     'schedule': crontab(minute='*/3'),
    #     # 'schedule': crontab(minute=45, hour=6),
    #     # "schedule":2 
    # },
    '13f-strategy': 
    {
        'task': 'Alerts.tasks.get_13f',
        'schedule': crontab(minute=45, hour=2),
        # 'schedule': crontab(minute='*/10'),
    },
    # 'Relative_Volume': {
    #     'task': 'Alerts.tasks.Relative_Volume',
    #     'schedule': crontab(minute='*/30'),
    #     # "schedule":10 
    # },
    # 'Unusual_Option_Buys': {
    #     'task': 'Alerts.tasks.Unusual_Option_Buys',
    #     'schedule': crontab(minute=0, hour='*/2'),
    #     # "schedule":20
    # },
    # 'Short_Interest': {
    #     'task': 'Alerts.tasks.Short_Interset',
    #     # 'schedule': crontab(minute='*/15'),
    #     "schedule": 10
    # },
    # 'Insider_buyers': {
    #     'task': 'Alerts.tasks.Insider_Buyer',
    #     'schedule': crontab(minute='*/25'),
    #     # "schedule":20 
    # },
    # 'MajorSupport_1hour': {
    #     'task': 'Alerts.tasks.MajorSupport_1hour',
    #     # 'schedule': crontab(minute=0, hour='*/1'),
    #     "schedule":250 
    # },
    # 'MajorSupport_4hour': {
    #     'task': 'Alerts.tasks.MajorSupport_4hour',
    #     'schedule': crontab(minute=0, hour='*/4'),
    #     # "schedule":10 
    # },
    # 'MajorSupport_1day': {
    #     'task': 'Alerts.tasks.MajorSupport_1day',
    #     'schedule': crontab(minute=15, hour=12),
    #     # "schedule":2 
    # },
    # 'Upgrade_Monthly_Plan': {
    #     'task': 'Payment.tasks.upgrade_to_monthly',
    #     'schedule': crontab(minute=0, hour='*/12'),
    #     # "schedule":2 
    # },
}

### configuration of celery_once that make task of twitter scraping runs indefinitely ###
# CELERY_ONCE_CONFIG = {
#     'backend': 'celery_once.backends.Redis',
#     'settings': {
#         'url': 'redis://redis:6379/',  # Redis URL for the lock
#         'default_timeout': 60 * 60 * 24 * 365 * 50,  # 50 years in seconds
#     }
# }


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'local_mem_cache',
    }
}
# S3 Configuration for media files
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_PRESIGNED_EXPIRY = timedelta(minutes=15)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/Media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Media')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
    'ACL': 'public-read-write',
}
