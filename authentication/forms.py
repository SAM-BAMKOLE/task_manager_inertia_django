from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User  # Import your custom user model
from django import forms
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no `username` field.
    """
    class Meta:
        model = User
        fields = ("email",'first_name', 'last_name')  # Specify the fields to be used for creation


class CustomUserChangeFormInApp(UserChangeForm):
    """
    A form for updating a user, with no `username` field.
    Only use this form in the app
    """
    class Meta:
        model = User
        # Include all fields you want to be editable in the admin
        fields = ("email", "first_name", "last_name")

class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating a user, with no `username` field.
    Only use this form in admin
    """
    class Meta:
        model = User
        # Include all fields you want to be editable in the admin
        fields = ("email", "first_name", "last_name", "is_active", "is_staff", "is_superuser")

class CustomAuthenticationForm(AuthenticationForm):
    """
    A form for authenticating a user
    """
    username = forms.EmailField(label="Email")

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password')

            else:
                self.confirm_login_allowed(self.user_cache)
                return self.cleaned_data