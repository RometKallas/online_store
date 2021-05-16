from django import forms
from .models import UserBase

class RegistrationFrom(forms.ModelForm):

    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    #describe what model are we going to use
    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)