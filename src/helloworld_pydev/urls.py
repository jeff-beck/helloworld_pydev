from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld_pydev.views.home', name='home'),
    # url(r'^helloworld_pydev/', include('helloworld_pydev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # public-facing urls
    url(r'^hello_polls/$', 'hello_polls.views.index'),
    url(r'^hello_polls/(?P<poll_id>\d+)/$', 'hello_polls.views.detail'),
    url(r'^hello_polls/(?P<poll_id>\d+)/results/$', 'hello_polls.views.results'),
    url(r'^hello_polls/(?P<poll_id>\d+)/vote/$', 'hello_polls.views.vote'),
)
