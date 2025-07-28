from django.forms import ModelForm
from .models import listing

class ListingForm(ModelForm):
    class Meta:
        model = listing
        fields = ["title","price","num_bedrooms","num_bathrooms","square_footage","address","image"]