# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# actions.py

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideName(Action):
    def name(self) -> str:
        return "action_provide_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        name = tracker.get_slot("name")
        dispatcher.utter_message(text=f"¡Encantado de conocerte, {name}!")
        return []


