# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Chicago'
USE_I18N = True
SITE_ID = 1

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0es_f@c+!_jyv0*ms%on6g5p$*-o+cls2!#1+&&28s)q7zn4zm'

#==============================================================================
# Calculation of directories relative to the module location
#==============================================================================
import os
import sys
import perfo_analysis

PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.realpath(perfo_analysis.__file__))
)

VAR_ROOT = os.path.join(os.environ['VIRTUAL_ENV'], 'var')
if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'perfo_analysis.conf.urls'

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'static'),
#    os.path.join(PROJECT_DIR, '..',
#        'django-cms', 'cms' , 'media'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    # 'Custom context processors here',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'south',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'cms',
    'menus',
    'cms.plugins.text',
    'cms.plugins.teaser',
    'mptt',
    'sekizai',

    'perfo_analysis.apps.cms_spam_pages',
)

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'debug_logging',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

if DEBUG:
    MIDDLEWARE_CLASSES += (
        'debug_logging.middleware.DebugLoggingMiddleware',
    )

#==========================================================================
# django-cms settings
#==========================================================================

CMS_MEDIA_PATH = 'cms/'
CMS_PAGE_MEDIA_PATH = 'cms_page_media/'
CMS_MEDIA_ROOT = STATIC_ROOT + CMS_MEDIA_PATH
CMS_MEDIA_URL = STATIC_URL + CMS_MEDIA_PATH


CMS_TEMPLATES = (
    ('template_nomenu_0placeholder.html', 'No menu with 0 placeholder'),
    ('template_menu_0placeholder.html', 'Menu with 0 placeholder'),
    ('template_menu_1placeholder.html', 'Menu with 1 placeholder'),
    ('template_menu_10placeholders.html', 'Menu with 10 placeholders'),
    ('template_nomenu_1placeholder.html', 'No menu with 1 placeholder'),
    ('template_nomenu_10placeholders.html', 'No menu with 10 placeholders'),
)

LANGUAGES = [
    ('en', 'English'),
]

CMS_MODERATOR = False

#==========================================================================
# django-debug-toolbar settings
#==========================================================================
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_PANELS = (
        'debug_logging.panels.cache.CacheLoggingPanel',
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_logging.panels.timer.TimerLoggingPanel',
        'debug_logging.panels.settings_vars.SettingsVarsLoggingPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_logging.panels.sql.SQLLoggingPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        'debug_logging.panels.revision.RevisionLoggingPanel',
        'debug_logging.panels.identity.IdentityLoggingPanel',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
        #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
        'HIDE_DJANGO_SQL': False,
    }

    DEBUG_LOGGING_CONFIG = {
        'SQL_EXTRA': True,
        'CACHE_EXTRA': True,
    }
