from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'klb12.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$','qpple.views.regist'),
    url(r'^login/$','qpple.views.login'),
    url(r'^index/$','qpple.views.index'),
    url(r'^logout/$','qpple.views.logout'),

    url(r'^admin/', include(admin.site.urls)),
)
