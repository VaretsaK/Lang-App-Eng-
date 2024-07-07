from django import forms
from users.models import UserProfile, PhoneNumber

from django.contrib.auth.models import User
from django.forms import modelformset_factory

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture',)
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ('number',)
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
        }


PhoneNumberFormSet = modelformset_factory(
    PhoneNumber, form=PhoneNumberForm, extra=1)

