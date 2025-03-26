'''
Write a function called nearestBusStop(street) that has one parameter, a street represented 
as a positive integer. 

Your function should return the nearest bus stop to the given street. 
Buses stop every eighth street (i.e. streets 0, 8, 16 etc.). When the street is the same 
distance from two bus stops, return the lower street number. For example, the nearest bus 
stop to street 4 would be 0, and the nearest bus stop to street 13 would be 16.
'''

def nearestBusStop(street):
    if street % 8 == 0: 
        stop = street
    if street % 8 <= 4:
        stop = street
    if street % 8 > 4:
        stop = street +1
    return stop

print(nearestBusStop(4))