from app import app
import urllib.request, json
from models import Location
from flask import config

Location = location.Location

api_key = config["AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY"]
base_url = config["https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings"]