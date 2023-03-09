from django.contrib import admin
from .models import Profile, CustomUser
from .forms import CustomCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'last_name', 'first_name', 'is_staff', 'is_active', 'is_email_verified', 'is_teacher', 'last_login', 'date_joined')
    list_filter = ('email', 'last_name', 'is_staff', 'is_active', 'is_email_verified', 'is_teacher',)
    fieldsets = (
        (None, {'fields': ('email', 'last_name', 'first_name', 'father_name', 'password', 'classes', 'subjects',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_email_verified', 'is_teacher',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'last_name', 'first_name', 'father_name', 'password1', 'password2', 'classes', 'subjects', 'is_staff', 'is_active', 'is_email_verified', 'is_teacher',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email', )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
