from django import forms
#
# class identity_login(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())