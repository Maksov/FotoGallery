from django.conf.urls import patterns, include, url
from gallery.settings import ROOT_URL

urlpatterns = patterns('',
    url(r'^%s' % ROOT_URL[1:], include('gallery.real_urls')),
)
