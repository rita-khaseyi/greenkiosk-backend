from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'location', 'date_of_birth')

    def username(self, obj):
        return obj.user.username

    username.short_description = 'Username'

admin.site.register(UserProfile, UserProfileAdmin)
