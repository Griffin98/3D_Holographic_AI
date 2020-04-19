
from zomathon import ZomatoAPI
from geopy.geocoders import Nominatim

def findNearbyRestaurant(location):
    zom = ZomatoAPI("df4b95e9cbcc6a7c090647586f563d23")
    geolocator = Nominatim(user_agent="HoloVA")
    location = geolocator.geocode(location)

    coordinate = "{lat} {lon}".format(lat=location.latitude, lon=location.longitude)

    nearby = zom.geocode(coordinate=coordinate)
    print(nearby['nearby_restaurants'])

    return 1
    """try:
        for num, restaurant in enumerate(nearby['nearby_restaurants']):
            data = '{number}. {name} - {addr}'.format(
                number=num + 1,
                name=restaurant['restaurant']['name'],
                addr=restaurant['restaurant']['location']['address']
            )
    except:
        print('Something went wrong when fetching nearby restaurant...')

    return data"""

if __name__ == "__main__":
    x = findNearbyRestaurant("pune")
    print(x)