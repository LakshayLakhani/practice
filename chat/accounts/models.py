from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group


class Chats(models.Model): #extra
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message


class ExtendGroup(Group):
    chat = models.ManyToManyField(Chats, blank=True) #extra
    created = models.DateTimeField(auto_now_add=True)
    # user = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.name

class UserDetails(models.Model):
    # user = models.ForeignKey(User, null=True, blank=True)
    user = models.OneToOneField(User, null=True, blank=True)
    user_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    mobile_no = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    group = models.ManyToManyField(Group, blank=True)

    def __unicode__(self):
        return u'%s' % (self.user.username)
