from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    phone = forms.CharField(required=True, label="Телефон")
    address = forms.CharField(required=False, widget=forms.Textarea, label="Адрес")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'address', 'password1', 'password2']
