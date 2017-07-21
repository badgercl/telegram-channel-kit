#!/your_path_to_python
# -*- coding: utf8 -*-

import requests
import telegram_config
import json

def send_post(txt):
    url = "https://api.telegram.org/bot{}/sendMessage"
    u = url.format(telegram_config.bot_token)
    p = {'chat_id':telegram_config.channel_id,'parse_mode':'html','disable_web_page_preview':True, 'text':txt}
    r = requests.post(u,data=p)
    if r.status_code == 200:
        if telegram_config.show_output:
            print(json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        print("Error sending post: {}\n{}".format(r.status_code, r.text))

