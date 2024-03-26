from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import Regular_User

class UserForm(ModelForm):
    class Meta:
        model = Regular_User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            })
        }