from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',                       'andreev_ru.main.views.home',              name='home'),

    url(r'^works/$',                 'andreev_ru.main.views.works',             name='works'),
    url(r'^work/(?P<slug>[-\w]+)/$', 'andreev_ru.main.views.work',              name='work'),

    url(r'^team/$',                  'andreev_ru.main.views.team',              name='team'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Redactor JS
    url(r'^redactor/', include('redactor.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += staticfiles_urlpatterns()
