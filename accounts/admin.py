from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUseradmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # this variable ---> admin change form fields
    fieldsets = UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password', 'phone_number', ), }),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'age', ), }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', ), }),
        ('Important Dates', {'fields': ('last_login', 'date_joined', ), }),
    )
    # this variable ---> admin create form fields
    add_fieldsets =  UserAdmin.add_fieldsets = (
        (None, {"classes": ("wide", ), 'fields': ('username', 'password1', 'password2', 'phone_number')}),
    )
    list_display = ('username', 'email', 'phone_number', 'is_staff')


admin.site.register(CustomUser, CustomUseradmin)