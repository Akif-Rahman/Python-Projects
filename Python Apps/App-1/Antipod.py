latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude.__mul__(int("-1"))

if longitude.__le__(float("0")):
    antipode_longitude = longitude.__add__(float("180")) 
    
else:
    antipode_longitude = longitude.__sub__(float("180"))


print(antipode_latitude)
print(antipode_longitude)
