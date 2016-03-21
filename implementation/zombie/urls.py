from django.conf.urls import patterns, include, url
from django.contrib import admin
from zombie import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^profile/(?P<username>[\w]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<username>[\w]+)/badges/$', views.badges, name='badges'),
    url(r'^profile/(?P<username>[\w]+)/friends/$', views.friends, name='friends'),
    url(r'^game/$', views.game, name='game'),
)