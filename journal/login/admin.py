from django.contrib import admin
from .models import Profile, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'last_name', 'first_name', 'father_name', 'is_staff', 'is_active', 'is_confirmed', 'is_teacher',)
    list_filter = ('email', 'last_name', 'first_name', 'father_name', 'is_staff', 'is_active', 'is_confirmed', 'is_teacher',)
    fieldsets = (
        (None, {'fields': ('email', 'last_name', 'first_name', 'father_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_confirmed', 'is_teacher',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'last_name', 'first_name', 'father_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_teacher',)}
        ),
    )
    search_fields = ('email', 'father_name')
    ordering = ('email', 'father_name')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
