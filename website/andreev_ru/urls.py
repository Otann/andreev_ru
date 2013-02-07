from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.decorators.cache import cache_page
from andreev_ru.main.views import *

admin.autodiscover()

urlpatterns = i18n_patterns('',

    url(r'^$',                       cache_page(60)(home),              name='home'),
    url(r'^/$',                      cache_page(60)(home),              name='home'),

    url(r'^works/$',                 cache_page(60)(works),             name='works'),
    url(r'^work/(?P<slug>[-\w]+)/$', cache_page(60)(work),              name='work'),

    url(r'^search/$',                cache_page(60)(search),            name='search'),
    url(r'^search_json/$',           search_json,                       name='search_json'),

    url(r'^news/$',                  cache_page(60)(news),              name='news'),
    url(r'^about/$',                 cache_page(60)(about),             name='about'),
    url(r'^contacts/$',              cache_page(60)(contacts),          name='contacts'),
    url(r'^team/',                   cache_page(60)(team),              name='team'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),

    url(r'^(?P<slug>[-\w]+)$',       cache_page(60)(page),              name='page'),
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
