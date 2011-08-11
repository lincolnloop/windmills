from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    # project urls here
    url(r'^', include('cms.urls')),
    url(r'debug-logging/$', include('debug_logging.urls')),
)
