from django.conf.urls import patterns, url

from . import views

# urlpatterns = patterns('',
#         url(r'^$', views.index, name='index'),
#         url(r'^(?P\d+)/$', views.chat_room, name='chat_room'),
#
#         )


urlpatterns = [
   url(r'^home/(?P<group_id>\d+)/$', views.home, name="home"),
    # url(r'^home/$', views.home, name='home'),
    url(r'^post/$', views.Post, name='chat_post'),
    url(r'^messages/(?P<group_id>\d+)/$', views.Messages, name='messages'),
    url(r'^someonetyping/$', views.Someonetyping, name='someonetyping'),
    url(r'^someone/$', views.Someone, name='someone'),
    url(r'^group/$', views.group, name='group'),
    ]
