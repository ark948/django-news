from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser

# UserCreationForm -> admin
# UserChangeForm -> user sign up

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )