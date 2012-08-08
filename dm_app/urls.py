from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to


admin.autodiscover()

urlpatterns = patterns('',
	# rework this to be main login front page:
	url(r'^$', 'chart.views.login_view', name="home"), 


	# user main page/dashboard/tracking display:
	url(r'^user/(?P<user_id>\d+)/$', 'chart.views.detail', name="user_detail"), 

	# in house update modual:
    url(r'^user/(?P<user_id>\d+)/update/$', 'chart.views.update', name="update"), 
    url(r'^user/(?P<user_id>\d+)/update_info/$', 'chart.views.update_info', name="update_info"), 
    # modual to download/save all your phi:
    url(r'^user/(?P<user_id>\d+)/download/$', 'chart.views.download', name="download"),
    
    url(r'^logout', 'chart.views.logout_view', name="logout"),

    url(r'^registration', 'chart.views.registration', name="registration"),

    url(r'^confirmation', 'chart.views.logout_view', name="confirmation"),
    # url(r'^accounts/', include('registration.urls')),

    # Examples:
    # url(r'^$', 'dm_app.views.home', name='home'),
    # url(r'^dm_app/', include('dm_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
