from perfo_analysis.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'perfo_analysis.conf.dev.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'perfo_analysis',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
