from django import forms
from django.contrib.auth.models import User
from Blog.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProFileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
