from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('email','username','is_admin','is_doctor')
    list_filter=('is_admin','is_doctor')

    fieldsets = (
        ('계정정보', {"fields": ('email','username'),}),
        ('권한',{ 'fields':('is_admin','is_doctor') }),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','username','password1','password2'),
        }
         ),
    )
    search_fields=('email','username',)
    ordering=('email',)
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

    
# Register your models here.
