from django import template

register = template.Library()

from django.contrib.auth.models import User

@register.simple_tag
def total_users():
    return User.objects.count()
