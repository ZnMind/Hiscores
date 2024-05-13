from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ValidationError
from django.contrib.auth.models import User

class PlayerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PlayerLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                ("This account is inactive"),
                code="inactive",
            )