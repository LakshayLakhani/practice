from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.login_user, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^signup/$', views.Signup, name='signup'),
    ]
