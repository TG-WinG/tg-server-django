from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser as User
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=('email','student_id','is_admin')
    list_filter=('is_admin','status','is_email_activated')

    fieldsets = (
        ('계정정보', {"fields": ('email','student_id','status','semester','phone_number'),}),
        ('권한',{ 'fields':('is_admin','is_email_activated') }),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','student_id','password1','password2'),
        }
         ),
    )
    search_fields=('email','student_id','semester','phone_number')
    ordering=('email','student_id','semester')
    filter_horizontal=()

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)

    
# Register your models here.
