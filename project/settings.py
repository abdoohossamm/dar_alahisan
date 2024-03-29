from pathlib import Path
import os
from configurations import Configuration # type: ignore
from configurations import values # type: ignore
# import dj_database_url


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-fbat_#98=sj_%@0=hueb*9t7%d_@wz=-7^*rlfrvm$n7!agzam'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ["127.0.0.1"]

    # Application definition

    INSTALLED_APPS = [
        'app',
        'reports',
        'widget_tweaks',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'crispy_forms',
        'crispy_bootstrap5',
        'debug_toolbar',
        'django_filters'
    ]

    MIDDLEWARE = [
        # debugging toolbar
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'project.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

    WSGI_APPLICATION = 'project.wsgi.application'
    


    # Database
    # https://docs.djangoproject.com/en/4.0/ref/settings/#databases

    # DATABASES = {
    #     'default': {
            # 'ENGINE': 'django.db.backends.postgresql',
            # 'NAME': 'eldar',
            # 'USER': 'postgres',
            # 'PASSWORD': '123456',
            # 'HOST': 'localhost',
            # 'PORT': '5432'
    #     }
    # }
    DATABASES = values.DatabaseURLValue(f'postgres://postgres:123456@localhost:5432/eldar')  
    #                                     postgres://USER:PASSWORD@HOST:PORT/NAME
    # DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    #   }


    # Password validation
    # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/4.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Etc/GMT-2'
    USE_L10N = True
    USE_I18N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.0/howto/static-files/

    STATIC_URL = 'static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
    # STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')
    # Default primary key field type
    # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    LOGOUT_REDIRECT_URL = 'login'
    LOGIN_REDIRECT_URL = 'index'
    LOGIN_URL = 'login'
    handler404 = 'app.views._404_not_found'
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]


# settings for production
class Prod(Dev):
    ALLOWED_HOSTS = ['abdoohossamm.pythonanywhere.com']
    DEBUG = False
    SECRET_KEY = values.SecretValue()
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'abdoohossamm$eldar',
            'USER': 'abdoohossamm',
            'PASSWORD': '#Aa1234556',
            'HOST': 'abdoohossamm.mysql.pythonanywhere-services.com',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                },
        }
    }
