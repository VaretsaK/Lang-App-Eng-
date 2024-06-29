from django import forms
from users.models import UserProfile

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User   #, UserProfile
        fields = ('username', 'email', 'password1', 'password2')  # TODO check ProfPic
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'profile_picture': forms.ImageField(attrs={'class': 'form-control'}),  # TODO check pic FileField
        }
