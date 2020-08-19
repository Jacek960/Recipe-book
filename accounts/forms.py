from django.contrib.auth.models import User
from django import forms

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ( 'email', 'first_name', 'last_name', )