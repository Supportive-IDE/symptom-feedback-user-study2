def nearestBusStop(street):
    if street % 8 == 0: 
        stop = street
    if street % 8 <= 4:
        stop = street
    if street % 8 > 4:
        stop = street +1
    return stop