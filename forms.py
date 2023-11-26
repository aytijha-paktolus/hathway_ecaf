from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=255, required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    role = forms.CharField(max_length=20, choices=(('admin', 'Admin'), ('user', 'User')), required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'address', 'zip_code', 'role')