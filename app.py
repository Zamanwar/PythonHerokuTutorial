import requests

base_url = "https://api.telegram.org/bot5214403693:AAE7RwwToN9EvXU_mkGKoKzge59w1xX5INo/"


def read_msg(offset):
    parameters = {
        "offset": offset

    }
    resp = requests.get(base_url + "getUpdates", data=parameters)
    data = resp.json()
    print(data)

    for result in data["result"]:
        if "Hit" in result["message"]["text"]:
            send_msg()
        else:
            new_msg()
    if data["result"]:
        return data["result"][-1]["update_id"] + 1


def send_msg():
    parameters = {
        "chat_id": "-756942555",
        "text": "Why the bot is so lazy"
    }
    resp = requests.get(base_url + "sendMessage", data=parameters)
    print(resp.text)


def new_msg():
    parameters = {
        "chat_id": "-756942555",
        "text": "Why the bot is so active"
    }
    resp = requests.get(base_url + "sendMessage", data=parameters)
    print(resp.text)


offset = 0

read_msg(offset)
