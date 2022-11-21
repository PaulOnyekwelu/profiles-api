from django.contrib import admin
from profiles import models


@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['email', 'first_name',
                    'last_name', 'is_staff', 'is_superuser']
    list_editable = ['last_name']
    list_filter = ['is_superuser', 'is_staff']


@admin.register(models.FeedModel)
class FeedAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('user_profile', 'status_text')
    list_filter = ('user_profile',)
