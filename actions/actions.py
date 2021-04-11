# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from validate_email import isValidEmail, isValidPhone
from database_connectivity import DataUpdate

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"
    
    @staticmethod
    def requiured_slots(Tracker):
        if Tracker.get_slot('first_name'):
            return [first_name]

    def slot_mappings(self) -> Dict[Text, List[Dict]]:
        return { "request_names": [self.from_intent(intent= "affirm", value=True), self.from_intent(intent= "deny", value=False)]}


    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(
                text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}

    
    def validate_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `Phone Number` value."""

        #Using regex for accurate slot value of phone.
        print(f"Phone given = {slot_value}")
        if not isValidPhone(slot_value):
            dispatcher.utter_message(
                text=f"Invalid Phone Number")
            return {"phone": None}
        else:
            return {"phone": slot_value}



    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `Email` value."""

        # Using regex for accurate slot value of email.
        print(f"Email given = {slot_value}")
        if not isValidEmail(slot_value):
            dispatcher.utter_message(
                text=f"Invalid Email")
            return {"email": None}
        else:
            return {"email": slot_value}

class UtterSubmit(Action):
    def name(self) -> Text:
        return "utter_submit_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,domain: DomainDict) -> List[Dict[Text, Any]]:
        print('running action submit')
        dispatcher.utter_message('Thank you for providing the info')
        dispatcher.utter_message(text="Your name is {0}. Your phone number is {1}. Your mail id is {2}.")
        tracker.get_slot("first_name"), tracker.get_slot("phone"), tracker.get_slot("email")
        DataUpdate(tracker.get_slot("first_name"), tracker.get_slot("phone"), tracker.get_slot("email"))
        dispatcher.utter_message('Thank you for providing the info')
        return []



        

