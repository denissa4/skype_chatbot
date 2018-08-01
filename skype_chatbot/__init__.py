import threading
import time
import requests
import skype_chatbot


class SkypeBot:
    
    def __init__(self, client_id, client_secret):

        def token_func():
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
                token_func()
                time.sleep(3590)

        self.t = threading.Thread(target=run_it)
        self.t.daemon = True
        self.t.start()

    @staticmethod
    def send_message(bot_id, bot_name, recipient, service, sender, text, text_format):
        return skype_chatbot.send_message(token, bot_id, bot_name, recipient, service, sender, text, text_format)

    @staticmethod
    def create_card_image(url, alt=None):
        return skype_chatbot.create_card_image(url, alt)

    @staticmethod
    def create_card_adaptive(items, actions):
        return skype_chatbot.create_card_adaptive(items, actions)

    @staticmethod
    def create_button(button_type, title, value):
        return skype_chatbot.create_buttons(button_type, title, value)

    @staticmethod
    def create_card_attachment(card_type, title, subtitle=None, text=None, images=None, buttons=None):
        return skype_chatbot.create_card_attachment(card_type, title, subtitle, text, images, buttons)

    @staticmethod
    def create_animation_card(card_type, url, images, title, subtitle, text, buttons, autoloop=True, autostart=True,
                         shareable=True):
        return skype_chatbot.create_animation(card_type, url, images, title, subtitle, text, buttons, autoloop,
                                          autostart, shareable)

    @staticmethod
    def send_media(bot_id, bot_name, recipient, service, sender, message_type, url, attachment_name):
        return skype_chatbot.send_media(token, bot_id, bot_name, recipient, service, sender, message_type, url,
                                    attachment_name)

    @staticmethod
    def send_card(bot_id, bot_name, recipient, reply_to_id, service, sender, message_type, card_attachment, text):
        return skype_chatbot.send_card(token, bot_id, bot_name, recipient, reply_to_id, service, sender, message_type,
                                   card_attachment, text)
        
    # Not yet supported

    @staticmethod
    def send_action(service, sender):
        return skype_chatbot.send_action(token, service, sender)

    @staticmethod
    def create_item_for_adaptive_card(items):
        return items

    @staticmethod
    def create_action_for_adaptive_card(actions):
        return actions
