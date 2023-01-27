from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A class-based form for creating new instances of the 'CustomUser' model.

    This form inherits from Django's 'UserCreationForm' and uses the
    'CustomUser' model. It includes the 'UserCreationForm' default fields (such
    as 'username', 'password1' and 'password2') plus a 'name' field from the
    'CustomUser' model.
    """
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name', )


class CustomUserChangeForm(UserChangeForm):
    """
    A class-based form for updating existing instances of the 'CustomUser'
    model.

    This form inherits from Django's 'UserChangeForm' and uses the 'CustomUser'
    model and its fields.
    """
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
