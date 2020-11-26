
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class HealthForm(FormAction):

    def name(self):
        return "health_form"  # returns the name of the form action

    @staticmethod
    def required_slots(tracker): #the slots that need to be filled before submit method is invoked
        if tracker.get_slot("confirm_exercise")==True:
            return["confirm_exercise","exercise","sleep","diet","stress","goal"]
        else:
            return ["confirm_exercise","sleep", "diet", "stress", "goal"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any],
    ) ->List[Dict]:
        return []

    def slot_mappings(self)-> Dict[Text, Union[Dict, List[Dict]]]: #Tells rasa how to extract slot values from user input
        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="affirm", value=False),
                self.from_intent(intent="inform", value=True)
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny",value="None")
            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny")
            ],
            "goal": [
                self.from_text(intent="inform"),
            ]


        }



