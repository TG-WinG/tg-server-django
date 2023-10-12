from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label='패스워드',widget=forms.PasswordInput)
    password2=forms.CharField(label='패스워드 확인',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields={'email','username'}
    
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("패스워드가 맞지 않습니다.")
        return password1
    
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields=('email','username','is_active','is_admin','is_doctor')






