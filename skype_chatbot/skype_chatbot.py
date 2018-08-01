import requests


def send_message(token, bot_id, bot_name, recipient, service, sender, text, text_format='markdown'):
    try:

        payload = {
                    "type": "message",
                    "text": text,
                    "from": {
                        "id": bot_id,
                        "name": bot_name,
                    },
                    "recipient": recipient,
                    "textFormat": text_format,  # markdown
                    "conversation": {
                        "id": sender
                    }
                    }
        r = requests.post(service+'/v3/conversations/'+sender+'/activities/',
                          headers={"Authorization": "Bearer " + str(token), "Content-Type": "application/json"},
                          json=payload)

        print('request status: ', r)

    except Exception as e:

        print('exception status: ', e)


def create_button(button_type, title, value):

    button_dict = dict()
    button_dict["type"] = button_type
    button_dict["title"] = title
    button_dict["value"] = value

    return button_dict


def create_card_image(url, alt):
    img_dict = dict()
    img_dict["url"] = url
    img_dict["alt"] = alt

    return img_dict


def create_card_attachment(card_type, title, subtitle, text, images, buttons):
    card_attachment = {
        "contentType": "application/vnd.microsoft.card." + card_type,
        "content": {
            "title": title,
            "subtitle": subtitle,
            "text": text,
            "images": images,
            "buttons": buttons
        }
    }

    return card_attachment


def send_media(token, bot_id, bot_name, recipient, service, sender, message_type, url, attachment_name):
    try:
        payload = {
            "type": "message",
            "from": {
                "id": bot_id,
                "name": bot_name,
            },
            "recipient": recipient,
            "conversation": {
                "id": sender
            },
            "attachments": [{
                "contentType": message_type,
                "contentUrl": url,
                "name": attachment_name
            }]
        }

        r = requests.post(service + '/v3/conversations/' + sender + '/activities/',
                          headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
                          json=payload)

        print('request status: ', r)

    except Exception as e:

        print('exception status: ', e)


def send_card(token, bot_id, bot_name, recipient, reply_to_id, service, sender, message_type, card_attachment, text):
    try:
        payload = {
                    "from": {
                        "id": bot_id,
                        "name": bot_name,
                    },
                    "recipient": recipient,
                    "type": "message",
                    "attachmentLayout": message_type,  # AttachmentLayout: carousel or list
                    "text": text,
                    "attachments": card_attachment,
                    "conversation": {
                        "id": sender
                    },
                    "replyToId": reply_to_id
                    }
        r = requests.post(service+'/v3/conversations/'+sender+'/activities/',
                          headers={"Authorization": "Bearer "+token, "Content-Type": "application/json"}, json=payload)

        print('request status: ', r)

    except Exception as e:

        print('exception status: ', e)


def create_animation_card(card_type, url, images, title, subtitle, text, buttons,
                          autoloop=True, autostart=True, shareable=True):

    card_animation = {
        "contentType": "application/vnd.microsoft.card." + card_type,
        "content": {
            "autoloop": autoloop,
            "autostart": autostart,
            "shareable": shareable,
            "media": [
                        {"profile": "gif",
                         "url": url}
                     ],
            "title": title,
            "subtitle": subtitle,
            "text": text,
            "images": images,
            "buttons": buttons
            }
        }
    
    return card_animation


def create_card_adaptive(items, actions):

    card_attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [
                items
            ],
            "actions": [
                actions
            ],
        }
    }

    return card_attachment


def create_item_for_adaptive_card(items):
    return items


def create_action_for_adaptive_card(actions):
    return actions
