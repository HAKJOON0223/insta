from django import forms
from .models import Profile

class profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'address', 'profile_photo')