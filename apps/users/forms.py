from django.contrib.auth.models import User
from django import forms

class UserReqistrationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Подтвердите Пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["passwords2"]:
            raise forms.ValidationError("Пароли не совпадает!")
        return cd["password2"]