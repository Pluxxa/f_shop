from django.contrib import admin
from .models import Product
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserRegistrationForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'is_active')
    list_filter = ('type', 'is_active')
    search_fields = ('name', 'description')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserRegistrationForm
    list_display = ('username', 'email', 'phone', 'address', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'address', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
