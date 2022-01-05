import phonenumbers

import folium

from test import number

from phonenumbers import geocoder

key="1a4cc0002c284b2d9027f4f2daceba0f"
num1=phonenumbers.parse(number)

mylocation=geocoder.description_for_number(num1,"en")

print(mylocation)

from phonenumbers import carrier

service_nmber=phonenumbers.parse(number,"RO")

print(carrier.name_for_number(service_nmber,"en"))

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(key)

query=str(mylocation)
result=geocoder.geocode(query)
print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

map=folium.Map(location=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup=mylocation).add_to((map))
map.save("Loc.html")
