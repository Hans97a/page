from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Personal Info",
            {
                "fields": (
                    "nickname",
                    "image",
                    'phone_number',
                    'personal_id',
                )
            },
        ),
    )