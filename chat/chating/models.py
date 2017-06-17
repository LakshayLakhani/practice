# from __future__ import unicode_literals
#
# from django.db import models
# from django.contrib.auth.models import User
# from accounts.models import UserDetails
#
# class Chat(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User)
#     message = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.message

# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.name

# class Group(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=128)
#     # chat = models.ManyToManyField(Chat, blank=True)
#     # user_details = models.ManyToManyField(UserDetails, blank=True)
#
#     def __unicode__(self):              # __unicode__ on Python 2
#         return self.name

# class Membership(models.Model):
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)
#
#     def __unicode__(self):              # __unicode__ on Python 2
#         return self.group.name
