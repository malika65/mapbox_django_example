from django.db import models
from django.db import models 
from mapbox_location_field.models import LocationField,AddressAutoHiddenField



map_attrs = {  
 "style": "mapbox://styles/mapbox/outdoors-v11",
 "zoom": 13,
 "center": [74.582748, 42.882004],
 "cursor_style": 'pointer',
 "marker_color": "red",
 "rotate": False,
 "geocoder": True,
 "fullscreen_button": True,
 "navigation_buttons": True,
 "track_location_button": True, 
 "readonly": True,
 "placeholder": "Pick a location on map below", }

class Location(models.Model):
    location = LocationField(map_attrs = map_attrs)
    address = AddressAutoHiddenField(map_id="unique_id_1",blank = True)
