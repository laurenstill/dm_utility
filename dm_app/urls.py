from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# rework this to be main login front page:
	url(r'^index$', 'chart.views.index'), 
	# user main page/dashboard/tracking display:
	url(r'^user/(?P<user_id>\d+)/$', 'chart.views.detail'), 
	# in house update modual:
    url(r'^user/(?P<user_id>\d+)/update/$', 'chart.views.update'), 
    # modual to download/save all your phi:
    url(r'^user/(?P<user_id>\d+)/download/$', 'chart.views.download'),
    

    # Examples:
    # url(r'^$', 'dm_app.views.home', name='home'),
    # url(r'^dm_app/', include('dm_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
