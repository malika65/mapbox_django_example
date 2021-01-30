from django import forms 
from .models import Location  
from mapbox_location_field.models import LocationField


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location','address')

