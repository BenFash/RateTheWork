from blog.models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'user_type')
