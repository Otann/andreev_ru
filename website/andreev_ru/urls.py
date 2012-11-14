from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = i18n_patterns('',

    url(r'^$',                       'andreev_ru.main.views.home',              name='home'),

    url(r'^works/$',                 'andreev_ru.main.views.works',             name='works'),
    url(r'^work/(?P<slug>[-\w]+)/$', 'andreev_ru.main.views.work',              name='work'),

    url(r'^team/$',                  'andreev_ru.main.views.team',              name='team'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),

    url('', include('django.contrib.flatpages.urls'))
)

urlpatterns += patterns('',
    url(r'^redactor/', include('redactor.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
    )
