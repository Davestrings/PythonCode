days = int(input("Enter the number of days since sept 25th 2009: "))
numHours = 24 * days
radiovelocity_perhour = 299792458 * 3600
velocity = 38241



distance_mile = velocity * numHours
distance_km = 1.609344 * distance_mile
distance_m = distance_km * 1000
astronomer_distance = 92955887.6 / distance_mile

radiocomtime = distance_m / radiovelocity_perhour

print("Distance cover since 25/9/2009 is ", distance_mile)
print("Distanc in Astronomical units is :", astronomer_distance)
print("Radio communication time is :", radiocomtime)
