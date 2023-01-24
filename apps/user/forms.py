from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=355)
    password = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)