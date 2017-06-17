from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Friendship(models.Model):
    from_friend = models.ForeignKey(User, related_name="friend_set")
    to_friend = models.ForeignKey(User, related_name="to_friend_set")
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '%s, %s' %(self.from_friend.username, self.to_friend.username)
        # return '%s' %(self.to_friend.username)

class Posts(models.Model):
    user = models.ForeignKey(User)
    to_friend_wall = models.ForeignKey(User, related_name="to_friend_wall_set",
        null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return '%s' %(self.status)
