import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2ur1(7#=$kwy)m1p0it07=jt8_)17%d@w7ga4az*6t5l+^sc&v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'blog',
    'registration',
    'write_blog',
    'user_profile',

    'tinymce',
    'django_social_share',
    'captcha',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_extensions',
    'django_webp',
    'image_optimizer',


    # allauth providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'OAuth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    },
    'github': {
        'SCOPE': [
            'user',
            'email',
            'repo',
            'read:org',
        ],
    }

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'compression_middleware.middleware.CompressionMiddleware',
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

ROOT_URLCONF = 'codestim.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_webp.context_processors.webp',
                'blog.context_processors.subscriber_form',
            ],
        },
    },
]

AUTH_USER_MODEL = "registration.User"

WSGI_APPLICATION = 'codestim.wsgi.application'

ALLOWED_HOSTS = ['192.168.1.104', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'Karan',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',

]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_STORAGE = 'compress_staticfiles.storage.CompressStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'global'),
    os.path.join(BASE_DIR, 'media')
]

MEDIA_URL = '/media/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/images')

LOGIN_URL = '/user/login'
LOGIN_REDIRECT_URL = '/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'shygamer.com@gmail.com'
EMAIL_HOST_PASSWORD = 'Karan123@@##$$'

OPTIMIZED_IMAGE_METHOD = 'pillow'

TINYMCE_JS_URL = os.path.join(STATIC_URL + 'tinymce/tinymce.min.js')
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT + 'tinymce')
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'height': 550,
    'custom_undo_redo_levels': 20,
    'selector': '#id_body',
    'plugins': '''
            link image imagetools codesample
            table code lists nonbreaking visualblocks
            visualchars code autolink lists charmap print hr
            anchor pagebreak
            ''',
    'toolbar': '''
            styleselect | bold italic underline | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image | codesample | code | pagebreak
            ''',
    'menubar': False,
    'images_upload_url': MEDIA_URL + 'uploads/',
    'images_file_types': 'jpg,svg,webp',
    'automatic_uploads': True,
    'image_width': '778',
}
