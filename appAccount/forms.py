from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField


class CostumeUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

