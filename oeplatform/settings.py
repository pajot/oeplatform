"""
Django settings for oeplatform project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

try:
    from .securitysettings import *  # noqa
except ImportError:
    import logging
    import os

    logging.error("No securitysettings found. Triggerd in oeplatform/settings.py")
    SECRET_KEY = os.environ.get("SECRET_KEY", "0")
    DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
    URL = os.environ.get("URL")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = (
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sessions.backends.signed_cookies",
    "django_bootstrap5",
    "rest_framework",
    "rest_framework.authtoken",
    "modelview",
    "modelview.templatetags.modelview_extras",
    "login",
    "base",
    "base.templatetags.base_tags",
    "widget_tweaks",
    "dataedit",
    "colorfield",
    "api",
    "ontology",
    "axes",
    "captcha",
    "django.contrib.postgres",
    "fontawesome_5",
    "django_better_admin_arrayfield",
    "oeo_viewer",
    "factsheet",
    "corsheaders",
    "bootstrap4"
)

MIDDLEWARE = (
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "login.middleware.DetachMiddleware",
    "axes.middleware.AxesMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware"
)

ROOT_URLCONF = "oeplatform.urls"

EXTERNAL_URLS = {
    "tutorials_index": "https://openenergyplatform.github.io/academy/",
    "tutorials_faq": "https://openenergyplatform.github.io/academy/",
    "tutorials_api1": "https://openenergyplatform.github.io/academy/tutorials/api/OEP_API_tutorial_part1/",  # noqa E501
    "tutorials_licenses": "https://openenergyplatform.github.io/academy/tutorials/metadata/tutorial_open-data-licenses/",
    # noqa E501
    "readthedocs": "https://oeplatform.readthedocs.io/en/latest/?badge=latest",
    "compendium": "https://openenergyplatform.github.io/organisation/",
}


def external_urls_context_processor(request):
    """Define hard coded external urls here.
    Use in templates like this: {{ EXTERNAL_URLS.<name_of_url> }}
    Also, you may want to add an icon indicating external links, e.g.
    """
    return {"EXTERNAL_URLS": EXTERNAL_URLS}


SITE_ID = 1

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "oeplatform.settings.external_urls_context_processor",
            ]
        },
    }
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000"
    ]

GRAPHENE = {"SCHEMA": "factsheet.schema.schema"}

WSGI_APPLICATION = "oeplatform.wsgi.application"

try:
    ONTOLOGY_FOLDER  # noqa
except NameError:
    ONTOLOGY_FOLDER = "/tmp"

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

AUTH_USER_MODEL = "login.myuser"
LOGIN_URL = "/user/login"
LOGIN_REDIRECT_URL = "/"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    )
}

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesBackend",
    # custom class extenging Django ModelBackend for login with username OR email
    "login.backends.ModelBackendWithEmail",
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
