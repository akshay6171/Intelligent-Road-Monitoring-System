import random

def get_gps_location():
    latitude = round(random.uniform(18.40, 18.60), 6)
    longitude = round(random.uniform(73.80, 74.00), 6)
    return latitude, longitude


