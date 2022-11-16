from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['email', 'first_name',
                    'last_name', 'is_staff', 'is_superuser']
    list_editable = ['last_name']
    list_filter = ['is_superuser', 'is_staff']
