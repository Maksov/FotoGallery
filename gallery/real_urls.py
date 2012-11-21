from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^', include('gallery.items.urls')),
)
