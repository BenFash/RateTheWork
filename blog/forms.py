from .models import Rating, Work
from django import forms


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('content','suggested_price')

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('title', 'work_image', 'categories', 'sub_category', 'content')

