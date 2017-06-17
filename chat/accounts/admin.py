from django.contrib import admin

from .models import UserDetails, ExtendGroup, Chats

class UserDetailsAdmin(admin.ModelAdmin):
    # list_display = ("pk", "get_title_or_nothing")
    exclude = ('group',)

    class Meta:
        model = UserDetails

admin.site.register(UserDetails, UserDetailsAdmin)
admin.site.register(ExtendGroup)
admin.site.register(Chats)

# Register your models here.
