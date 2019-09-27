from app import app
import urllib.request, json
from models import Location
from flask import config
from geolocation.main import GoogleMaps 
from geolocation.distance_matrix.client import DistanceMatrixApiClient

address = "Nairobi"
google_maps = GoogleMaps(api_key = 'AIzaSyDU63uIF4cTPGfAm8TZ4bQPK1nP_qm2ePE'
location = google_maps.search(location=address)
my_location = location.first()

for administrative_area in my_location.administrative_area:
print(“{}: {} ({})”.format(administrative_area.area_type,
administrative_area.name, administrative_area.short_name))

lat = 40.7060008 lng = -74.0088189

my_location = google_maps.search(lat=lat, lng=lng).first()

# api_key = config["AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY"]
# base_url = config["https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings"]