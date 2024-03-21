from django import forms
from blog.models import Profile
from .models import ContactAdmin


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'user_type')


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = ContactAdmin
        fields = ('subject', 'email', 'message')
