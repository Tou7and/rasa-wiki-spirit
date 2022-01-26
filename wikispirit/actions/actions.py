# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import wikipedia
import opencc
from datetime import datetime
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType
from rasa_sdk import Action

class ActionHello(Action):
    def name(self) -> Text:
        return "action_hello"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        utterance = "你好，很高興為你服務!"
        dispatcher.utter_message(text=utterance)
        return []


class ActionBye(Action):
    def name(self) -> Text:
        return "action_bye"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        utterance = "謝謝您的使用，再見!"
        dispatcher.utter_message(text=utterance)
        return []


class ActionShowFunctions(Action):
    def name(self) -> Text:
        return "action_show_functions"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        utterance = "我可以幫你查維基，看時間，以及打招呼跟道別!\n"
        utterance += "你可以試著跟我說 查維基 / 現在時間/ 你好 / 再見 !"
        dispatcher.utter_message(text=utterance)
        return []


class ActionAnswerTime(Action):
    def name(self) -> Text:
        return "action_answer_time"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        now_text = str(datetime.now())
        date, time = now_text.split(" ")
        year, month, day = date.split("-")
        hour, minute, second = time.split(":")
        utterance = "今天是 {} 月 {} 日，現在時間是 {} 點 {} 分".format(month, day, hour, minute)
        dispatcher.utter_message(text=utterance)
        return []


class ActionQueryWiki(Action):
    def name(self) -> Text:
        return "action_query_wiki"

    async def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        # keyword = tracker.get_slot("keyword")
        keyword = tracker.latest_message.get("text")

        try:
            wikipedia.set_lang("zh")
            res_zh = wikipedia.summary(keyword, sentences=3)
            converter = opencc.OpenCC('s2t.json')
            res_tw = converter.convert(res_zh)
        except:
            res_tw = "抱歉，在 wikipedia 上找不到對應的條目..."

        dispatcher.utter_message(text=res_tw)
        return []

class ActionGetKeyword(Action):
    def name(self) -> Text:
        return "action_get_keyword"

    async def run(
        self, 
        dispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        utterance = "請告訴我你想查詢的關鍵字"

        dispatcher.utter_message(text=utterance)
        return []

