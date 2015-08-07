from django import forms

class CreateForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=16, min_length=3)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Password", max_length=16, min_length=3, widget=forms.PasswordInput)
    password_ = forms.CharField(label="Confirm password", max_length=16, min_length=3, widget=forms.PasswordInput)