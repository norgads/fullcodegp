from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser


class CustomUserUpdateForm(UserChangeForm):
    class Meta:
            model = CustomUser
            fields = ('avatar', "username", "first_name", "last_name", 'bio')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar', 'bio')


class CustomAuthenticationForm(AuthenticationForm):
    pass  



