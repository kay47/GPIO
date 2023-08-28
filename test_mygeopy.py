#from geopy.distance import geodesic


#newport_ri = (41.49008, -71.312796)

#cleveland_oh = (41.499498, -81.695391)

#print(geodesic(newport_ri, cleveland_oh).miles)


import geopy
from geopy import Nominatim
from geopy.distance import great_circle

geolocator = Nominatim(user_agent="blaco")
Accra = geolocator.geocode("Accra")
Abuja = geolocator. geocode("Abuja")
Accra_cord = (Accra.longitude,Accra.latitude)
Abuja_cord = (Abuja.longitude,Abuja.latitude)
print(geodesic(Abuja_cord, Accra_cord).miles)


