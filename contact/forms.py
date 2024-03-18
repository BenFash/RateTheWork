from django import forms
from .models import UserContactAdmin

class UserContactAdminForm(forms.ModelForm):
    class Meta:
        model = UserContactAdmin
        fields = ('name', 'subject','email', 'message')