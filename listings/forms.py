from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'address',
            'description',
            'price',
            'bedrooms',
            'bathrooms',
            'garage',
            'sqft',
            'is_published'
        ]