from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username', 'last_login', 'date_join', 'is_active')
    list_display_links=('email','first_name','last_name')
    read_only_fields=('last_login','date_join')
    ordering=('date_join',)
    
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
# Register your models here.
admin.site.register(Accounts,AccountAdmin)