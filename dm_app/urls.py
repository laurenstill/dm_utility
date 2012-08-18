from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to


admin.autodiscover()

urlpatterns = patterns('',
	# rework this to be main login front page:
	url(r'^$', 'chart.views.login_view', name="home"), 
    
	# user main page/dashboard/tracking display:
	url(r'^user/$', 'chart.views.detail', name="user_detail"),

	# in house update modual:
    url(r'^user/update/$', 'chart.views.update', name="update"), 

    # medication tracking
    url(r'^user/meds/$', 'chart.views.meds', name="meds"),
   
    # modual to download/save all your phi:
    url(r'^user/download/$', 'chart.views.download', name="download"),
    
    url(r'^logout', 'chart.views.logout_view', name="logout"),

    url(r'^registration', 'chart.views.registration', name="registration"),

    url(r'^confirmation', 'chart.views.logout_view', name="confirmation"),
    

    # url(r'^$', 'dm_app.views.home', name='home'),
    # url(r'^dm_app/', include('dm_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
