from django.conf.urls import patterns, url

from . import views
urlpatterns = [
    # url(r'^home/$', views.home, name='home'),
    url(r'^$', views.profile, name='profile'),
    url(r'^main-home/$', views.mainhome, name='main_home'),
    url(r'^post/$', views.post, name='post'),
    url(r'^load-more-user/$', views.load_more_user, name='load_more_user'),
    url(r'^(?P<id>\d+)/$', views.friends_profile, name='friends_profile'),
    url(r'^add-friend/(?P<id>\d+)/$', views.add_friends, name='add_friend'),
    url(r'^home-load-more-user/$', views.home_load_more_user, name='home_load_more_user'),
    url(r'^searching-friend/$', views.searching_friend, name='searching_friend'),
    # url(r'^someonetyping/$', views.Someonetyping, name='someonetyping'),
    # url(r'^someone/$', views.Someone, name='someone'),
    # url(r'^group/$', views.group, name='group'),
    ]
