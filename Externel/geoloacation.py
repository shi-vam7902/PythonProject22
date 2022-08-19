# from geopy.geocoders import Nominatim
# locator=Nominatim(user_agent="geoapiexercise")
# loactiontext = input("Enter Address :")
# location = locator.geocode(loactiontext)

# print(location.address)
# print(location.latitude)
# print(location.longitude)
from geopy.geocoders import Nominatim
locator=Nominatim(user_agent="geoapiexercise")
loactiontext = input("Enter Address :")
location = locator.geocode(loactiontext)

print(location.address)
print(location.latitude)
print(location.longitude)