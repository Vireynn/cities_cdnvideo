import math

def calculate_distance(lat1, lat2, lng1, lng2) -> float:
    R = 6371.0
    lat1, lat2, lng1, lng2 = map(math.radians, [lat1, lat2, lng1, lng2])

    dlat = lat2 - lat1
    dlng = lng2 - lng1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    c = 2 * math.atan2(a ** 0.5, (1 - a) ** 0.5)

    return R * c
