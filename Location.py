import phonenumbers

#geocoder : tp know the specific location to that phone number
from phonenumbers import geocoder

phone_number=phonenumbers.parse("+919359899826")
# india phone number ex +91
# nepal nepal phone number +977
# 
# #this will print the country name
print(geocoder.description_for_number(phone_number,'en'))