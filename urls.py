from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^', include('catalog.urls')),
    (r'^admin/', include(admin.site.urls)),
    )

if settings.DEBUG:
    urlpatterns += patterns ('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': '/Users/freebsdstuff/PycharmProjects/ecomstore/static'}),
    )

handler404 = 'views.file_not_found_404'
