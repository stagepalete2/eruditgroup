from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'get_full_name', 'email', 'phone', 'user_type', 'is_active'
    ]
    prepopulated_fields = {'slug' : ['username',]}