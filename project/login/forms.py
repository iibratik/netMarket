from django.forms import ModelForm, TextInput, PasswordInput
from registration.models import Regular_User  

class UserForm(ModelForm): 
    class Meta:
        model = Regular_User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'login-input',
                'placeholder': ''
            }),
            'password': PasswordInput(attrs={
                'class': 'login-input',
                'placeholder': ''
            }),
        }