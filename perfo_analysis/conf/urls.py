from django.conf import settings
from django.conf.urls.defaults import patterns, url, include

CONF_MODULE = '%s.conf' % settings.PROJECT_MODULE_NAME

urlpatterns = patterns('',
    # project urls here
    url(r'^debug-logging/', include('debug_logging.urls')),
    (r'', include('%s.common.urls.admin' % CONF_MODULE)),
    
    url(r'^', include('cms.urls')),
)
