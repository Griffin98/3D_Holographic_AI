from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet,AllSlotsReset

from include import Assistant_Settings
from Skills import *

class ActionWeather(Action):
    def name(self):
        return "skills_weather"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot('location')
        data = weather.get_weather(location)

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(data['description'],data['location'],data['temperature'],data['humidity'],data['wind_speed'])

        dispatcher.utter_message(response)
        return [SlotSet('location',location)]

class ActionRestaurant(Action):
    def name(self):
        return "skills_restaurant"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot('location')
        data = zomato.findNearbyRestaurant('location')

class ActionSlotsReset(Action):
    def name(self):
        return "reset_slots"

    def run(self,dispatcher,tracker,domain):
        return [AllSlotsReset()]
