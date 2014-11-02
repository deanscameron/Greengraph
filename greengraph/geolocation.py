"""Geolocation module"""

# Module takes the name of a give place and returns a url of a map of the area


# Get the coordinates of a given location
import geopy
geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
def geolocate(place):
  return geocoder.geocode(place,exactly_one=False)[0][1]
  
  
# Get the url of a map of the given location
import requests
def map_at(lat,long, satellite=False, zoom=12, 
           size=(400,400), sensor=False):
    base="http://maps.googleapis.com/maps/api/staticmap?"
    params=dict(
        sensor= str(sensor).lower(),
        zoom= zoom,
        size= "x".join(map(str,size)),
        center= ",".join(map(str,(lat,long))),
        style="feature:all|element:labels|visibility:off"
    )
    if satellite:
        params["maptype"]="satellite"
    return requests.get(base,params=params)

map_response=map_at(51.5072, -0.1275, zoom=10)
url=map_response.url