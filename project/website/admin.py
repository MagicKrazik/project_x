from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'payment_status', 'is_active', 'registration_date', 'last_payment_date']
    list_filter = ['payment_status', 'is_active', 'registration_date']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'payment_status', 'last_payment_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email', 'phone_number', 'payment_status')}),
    )
    actions = ['activate_users']

    def activate_users(self, request, queryset):
        queryset.update(is_active=True, payment_status='confirmed')
    activate_users.short_description = "Activate selected users and confirm payment"

admin.site.register(CustomUser, CustomUserAdmin)