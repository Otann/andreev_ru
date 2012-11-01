from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',                       'andreev_ru.main.views.home', name='home'),
    url(r'^page/(?P<slug>[-\w]+)/$', 'andreev_ru.main.views.page',  name='page'),

    url(r'^works/$',                 'andreev_ru.main.views.works', name='works'),
    url(r'^work/(?P<slug>[-\w]+)/$', 'andreev_ru.main.views.work',  name='work'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
