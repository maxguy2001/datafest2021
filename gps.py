import googlemaps
import re

import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import time

def googlemaps_query(provider_name):

    gmaps = googlemaps.Client(key='')

    # Geocoding an address

    # We implement region biasing:
        # Source: https://developers.google.com/maps/documentation/geocoding/overview#RegionCodes
    geocode_result = gmaps.geocode(provider_name, region="uk")

    lat = (geocode_result[0]["geometry"]["location"]["lat"])
    lng = (geocode_result[0]["geometry"]["location"]["lng"])

    return (lat, lng)

# AB10, PH26
tic = time.perf_counter()
print(googlemaps_query("IG4"))
toc = time.perf_counter()
print(f"Time {toc - tic:0.4f}")

def osm_query(postcode):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(postcode)

    return (location.latitude, location.longitude)

tic = time.perf_counter()
print(osm_query("IG4"))
toc = time.perf_counter()
print(f"Time {toc - tic:0.4f}")
