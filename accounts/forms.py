from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help texts for all fields
        for field_name, field in self.fields.items():
            field.help_text = None