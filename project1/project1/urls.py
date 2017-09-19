from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.sitemaps.views import index
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^resume/', include('resume.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
