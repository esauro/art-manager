from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    )

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

#if settings.DEBUG:
#    urlpatterns = patterns('',
#            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#            url(r'', include('django.contrib.staticfiles.urls')),
#    ) + urlpatterns
