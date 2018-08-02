# skype_chatbot

Python Skype Bot API for developing bots.

### Recommendation:
Read through this guide before beginning bot development [Register an application in Azure AD](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-authentication?view=azure-bot-service-3.0), [Messages and activities](https://docs.microsoft.com/en-us/azure/bot-service/dotnet/bot-builder-dotnet-activities?view=azure-bot-service-3.0)

### Overview:
1. This API is tested with Python 3.6.
2. Take ```app_id``` and ```app_secret``` from the app you will create on [Register a Bot](https://dev.botframework.com/bots/new)
3. For sending and receiving requests will using Flask application(A template ```main.py``` is provided. You can use one as your bot web-page).

### Simple Echo Bot

```
import skype_chatbot
import json
from flask import Flask, request 

app = Flask(__name__)

app_id = 'example_app_id'
app_secret = 'example_app_secret'

bot = skype_chatbot.SkypeBot(app_id, app_secret)

@app.route('/api/messages', methods=['POST', 'GET'])
def webhook():
  if request.method == 'POST':
    try:
        data = json.loads(request.data) 
        bot_id = data['recipient']['id']
        bot_name = data['recipient']['name']
        recipient = data['from']
        service = data['serviceUrl']
        sender = data['conversation']['id']
        text = data['text']

        bot.send_message(bot_id, bot_name, recipient, service, sender, text)
        
    except Exception as e:
      print(e)

  return 'Code: 200'
  
if __name__ == '__main__':

    context = ('domain.cer', 'domain.key')

    app.run(host='0.0.0.0', port=8000, debug=False, ssl_context=context)
```
# How to use

### Install package

Run in console:
```pip install skype_chatbot```     
  or download package from GitHub and copy folder `skype_chatbot` to `site-packages` (e.g. **C:\Python36\Lib\site-packages\skype_chatbot**)

### Create <main.py> file

Import skype_chatbot package:
```
import skype_chatbot
```

During installation input you app ID and secret key, once prompted:
```
app_id = "example_app_id"
app_secret = "example_app_secret"
```
Create object bot:
```bot = skype_chatbot.SkypeBot(client_id, client_secret)```

#### Now you can use base methods:
|                                 |
| ------------------------------- |
| send_message                    |
| send_media                      |
| create_animation_card           |
| create_card_attachment          |
| create_card_image               |
| create_button                  |
| send_card                       |
| create_card_adaptive            |
| create_item_for_adaptive_card   |
| create_action_for_adaptive_card |

### Send message:
`send_message(bot_id, bot_name, recipient, service, sender, text, text_format)`

*bot_id* - skype bot id, you can get it from request ```data['recipient']['id']```.     
  *bot_name* - skype bot name, you can get it from request ```data['recipient']['name']```.     
  *recipient* - user, to whom you are sending the message. You can get it from request ```data['from']```.     
  *service* - service url, you can get it from request ```data['serviceUrl']```.     
  *sender* - conversation id, you can get it from request ```data['conversation']['id']```.     
  *text* - text what you want to send recipient. Must be a string.     
  *text_format* - supported values: "plain", "markdown", or "xml" (default: "markdown").     

### Send media files:
`send_media(bot_id, bot_name, recipient, service, sender, message_type, url, attachment_name)`

*bot_id* - skype bot id, you can get it from request ```data['recipient']['id']```.     
*bot_name* - skype bot name, you can get it from request ```data['recipient']['name']```.     
*recipient* - user, to whom you are sending the message. You can get it from request ```data['from']```.     
*service* - service url, you can get it from request ```data['serviceUrl']```.     
*sender* - conversation id, you can get it from request ```data['conversation']['id']```.     
*message_type* - type of your media file, e.g. "image/png".     
*url* - open url for your media file.     
*attachment_name* - name, which is displayed to recipient.     

### Create card that can play animated GIFs or short videos:
`create_animation_card(card_type, url, images, title, subtitle, text, buttons, autoloop, autostart, shareable)`

*card_type* - type of card attachment ("hero", "thumbnail", "receipt").     
  *url* - open url for your animation file.     
  *images* - list of images, in card attachment (to create image use method `create_card_image`). Must be a list.     
  *title* - title for your card. Must be a string.     
  *subtitle* - subtitle for your card. Must be a string.     
  *text* - text for your card. Must be a string.     
  *buttons* - list of buttons, in card attachment (to create button use method `create_button`). Must be a list.     
  *autoloop* - default: True.     
  *autostart* - default: True.     
  *shareable* - default: True.     

### Create card attachment("hero", "thumbnail", "receipt"):
`create_card_attachment(card_type, title, subtitle, text, images, buttons)`

*card_type* - type of card attachment ("hero", "thumbnail", "receipt").     
  *title* - title for your card. Must be a string.     
  *subtitle* - subtitle for your card. Must be a string.     
  *text* - text for your card. Must be a string.     
  *images* - list of images, in card attachment (to create image use method `create_card_image`). Must be a list.     
  *buttons* - list of buttons, in card attachment (to create button use method `create_button`). Must be a list.     

### Create image for card:
`create_card_image(url, alt)`

  *url* - open url for your image.     
  *alt* - alternative text for image.     

### Create button(actions) for card:
`create_button(button_type, title, value)`

*button_type* - type of your button(e.g. "openUrl", "postBack").     
  *title* - name of button.     
  *value* - value of button(e.g. if button_type="openUrl", value="example.com").     

| Action Type   | Content of value property |
| ------------- |---------------------------|
| openUrl       | URL to be opened in the built-in browser.|
| imBack        | Text of the message to send to the bot (from the user who clicked the button or tapped the card). This message (from user to bot) will be visible to all conversation participants via the client application that is hosting the conversation. |
| postBack      | Text of the message to send to the bot (from the user who clicked the button or tapped the card). Some client applications may display this text in the message feed, where it will be visible to all conversation participants.
| call          | Destination for a call in following format: "tel:123123123123"   |
| playAudio     | URL of audio to be played |
| playVideo     | URL of video to be played
| showImage     | show image referenced by URL |
| downloadFile  | URL of file to be downloaded |
| signin        | URL of OAuth flow to be initiated |

### Send card attachment to recipient:
`send_card(bot_id, bot_name, recipient, reply_to_id, service, sender, message_type, card_attachment, text)`

*bot_id* - skype bot id, you can get it from request ```data['recipient']['id']```.     
  *bot_name* - skype bot name, you can get it from request ```data['recipient']['name']```.     
  *reply_to_id* - the message id you are replying to, you can get it from request ```data['id']```.     
  *recipient* - user, to whom you are sending the message. You can get it from request ```data['from']```.     
  *service* - service url, you can get it from request ```data['serviceUrl']```.     
  *sender* - conversation id, you can get it from request ```data['conversation']['id']```.     
  *message_type* - if you send more than one card, choose display way("carousel" or "list").     
  *card_attachment* - list of cards, in message (to create cards use method `create_card_attachment`). Must be a list.     
  *text* - text of your message.     



