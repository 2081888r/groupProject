from django.conf.urls import patterns, include, url
from django.contrib import admin
from zombie import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
#    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : '/accounts/password_change/done/'},  name="password_change"), 
#    url(r'^accounts/password_change/done/$', 'django.contrib.auth.views.password_change_done'),
#    url(r'^add_profile/$', views.register_profile, name='add_profile'),
#    url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
#    url(r'^profile_update/', views.profile_update, name='profile_update'),
#    url(r'^404/$', views.error_page, name='404'),
)