from .models import Rating
from django import forms


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('content','suggested_price')