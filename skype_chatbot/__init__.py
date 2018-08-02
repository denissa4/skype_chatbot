import threading
import time
from .skype_chatbot import *


class SkypeBot:
    
    def __init__(self, client_id, client_secret):

        def get_token():
            global token

            payload = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret + \
                      "&scope=https%3A%2F%2Fapi.botframework.com%2F.default"
            response = requests.post("https://login.microsoftonline.com/common/oauth2/v2.0/token?client_id=" +
                                     client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials&"
                                     "scope=https%3A%2F%2Fgraph.microsoft.com%2F.default", data=payload,
                                     headers={"Host": "login.microsoftonline.com",
                                              "Content-Type": "application/x-www-form-urlencoded"})
            data = response.json()
            token = data["access_token"]

        def run_it():
            while True:
                get_token()
                time.sleep(3590)

        self.t = threading.Thread(target=run_it)
        self.t.daemon = True
        self.t.start()

    @staticmethod
    def send_message(bot_id, bot_name, recipient, service, sender, text, text_format):
        return send_message(token, bot_id, bot_name, recipient, service, sender, text, text_format)

    @staticmethod
    def create_card_image(url, alt=None):
        return create_card_image(url, alt)

    @staticmethod
    def create_card_adaptive(items, actions):
        return create_card_adaptive(items, actions)

    @staticmethod
    def create_button(button_type, title, value):
        return create_button(button_type, title, value)

    @staticmethod
    def create_card_attachment(card_type, title, subtitle=None, text=None, images=None, buttons=None):
        return create_card_attachment(card_type, title, subtitle, text, images, buttons)

    @staticmethod
    def create_animation_card(card_type, url, images, title, subtitle, text, buttons, autoloop=True, autostart=True,
                              shareable=True):
        return create_animation_card(card_type, url, images, title, subtitle, text, buttons, autoloop,
                                     autostart, shareable)

    @staticmethod
    def send_media(bot_id, bot_name, recipient, service, sender, message_type, url, attachment_name):
        return send_media(token, bot_id, bot_name, recipient, service, sender, message_type, url,
                          attachment_name)

    @staticmethod
    def send_card(bot_id, bot_name, recipient, reply_to_id, service, sender, message_type, card_attachment, text):
        return send_card(token, bot_id, bot_name, recipient, reply_to_id, service, sender, message_type,
                         card_attachment, text)

    @staticmethod
    def create_item_for_adaptive_card(items):
        return items

    @staticmethod
    def create_action_for_adaptive_card(actions):
        return actions
