#!/your_path_to_python
# -*- coding: utf8 -*-

import requests
import json
import telegram_config

def print_updates():
    url = "https://api.telegram.org/bot{}/getUpdates"
    u = url.format(telegram_config.bot_token)
    r = requests.get(u)
    if r.status_code == 200:
        print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))        
    else:
        print("Error getting updates: {}\n{}".format(r.status_code, r.text))

print_updates()
