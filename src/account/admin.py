from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile,AccountCustom


class AccountCustomAdmin(UserAdmin):
    list_display = ['email','is_active']
    fieldsets = (
        (None, {
            "fields": (
                'email','username','password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_active','is_superuser','is_staff'
            ),
        }),
    
    )
    

admin.site.register(AccountCustom,AccountCustomAdmin)
admin.site.register(Profile)