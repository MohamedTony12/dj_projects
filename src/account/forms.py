from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AccountCustom

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='email',widget=forms.EmailInput())
    password1 = forms.CharField(label='password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='repeat password',widget=forms.PasswordInput())

    class Meta:
        model = AccountCustom
        fields = ['email','password1','password2']
        

class LoginForm(forms.Form):
    email = forms.EmailField(label='email',widget=forms.EmailInput())
    password = forms.CharField(label='password',widget=forms.PasswordInput())

    
