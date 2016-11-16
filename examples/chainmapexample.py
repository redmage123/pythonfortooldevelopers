#!/usr/bin/python3

from collections import ChainMap

# Here are three  separate dictionaries that contain a car part name 
# and a part number.
car_parts ={'hood':'1P994','engine':'2X2001','front_door':'1Y8884'}
car_options={'air_conditioning':'9B0003','Turbo':'1D9110','rollbar':'5Z0123'}
car_accessories = {'Cover':'4T1413','hood_ornament':'5N0512','seat_cover':'7C0316','hood':'blahblahblah'}


# Here we use the chainmap to combine the three dictionaries into one.  
car_manifest = ChainMap(car_parts,car_options,car_accessories)

print (car_manifest['engine'])

car_manifest['Cover'] = '4T1414'
print (car_manifest['Cover'])

print (car_manifest.maps[0])
print (car_manifest['hood'])
