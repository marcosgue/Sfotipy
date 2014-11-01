from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^singup/', 'userprofiles.views.singup', name='singup'),
    url(r'^singin/', 'userprofiles.views.singin', name='singin'),
)
