# This is Simple Echo Bot

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
