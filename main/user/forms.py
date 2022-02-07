from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class CreateUserForm(forms.ModelForm):
    _password = forms.CharField(label='Pass Conf', widget=forms.PasswordInput)
    password = forms.CharField(label='Pass', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'friend_code', 'full_name', 'role')

    def clean_password(self):
        password = self.cleaned_data.get("password")
        _password = self.cleaned_data.get("_password")
        if password != _password:
            raise ValidationError("Passwords don't match")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ChangeUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'friend_code', 'full_name', 'role')
