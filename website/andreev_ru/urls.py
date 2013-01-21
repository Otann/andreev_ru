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

    url(r'^search/$',                'andreev_ru.main.views.search',            name='search'),
    url(r'^search_json/$',           'andreev_ru.main.views.search_json',       name='search_json'),

    url(r'^(?P<slug>[-\w]+)$',       'andreev_ru.main.views.page',              name='page'),
)

urlpatterns += patterns('',
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT, }),
    )
