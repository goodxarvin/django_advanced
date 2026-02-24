from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('email',)
    search_fields = ('email',)
    fieldsets = (
        ("authentication", {
            'fields': ('email', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser'),
        }),
        ('group permissions', {
            'fields': ('groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ("last_login",),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser'),
        }),
    )

admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'first_name', 'last_name', 'country', 'created_at', 'updated_at')
    list_filter = ('country',)
    ordering = ('user',)
    search_fields = ('user', 'first_name', 'last_name', 'country')
    # fieldsets = (
    #     ('user', {
    #         'fields': ('user',),
    #     }),
    #     ('profile', {
    #         'fields': ('first_name', 'last_name','country'),
    #     }),
    # )

admin.site.register(Profile, ProfileAdmin)