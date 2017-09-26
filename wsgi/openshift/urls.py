from django.conf.urls import include, url

from django.contrib import admin
from views import home, logout, toggle

admin.autodiscover()

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^$', home, name='home'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^toggle/$', toggle, name='toggle'),
    url(r'^admin/', include(admin.site.urls)),
]
