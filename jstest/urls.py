from django.conf.urls import patterns, include, url

from django.contrib import admin
from signups.views import index, join
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jstest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^join/', join)
    #url(r'^admin/', include(admin.site.urls)),
)
