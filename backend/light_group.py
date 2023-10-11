import json
import os
import colorsys

import requests
from dotenv import load_dotenv


USERNAME = os.environ.get("HUE_USERNAME")

IP_ADDRESS = os.environ.get("HUE_IP_ADDRESS")

class LightGroup:
    def __init__(self, group_id):
        self.group_id = group_id
        self.on = True
        self.hue = 30000
        self.sat = 254
        self.bri = 254
        self.username = USERNAME
        self.ip_adress = IP_ADDRESS
        self.transition_time = 1

    def update_values(self, on: bool, color: str):
        self.on = on
        color = color.replace("#", "")
        r,g,b = tuple(int(color[i:i+2], 16)/255 for i in (0, 2, 4))
        h,s,v = colorsys.rgb_to_hsv(r, g, b)
        print(r,g,b)
        print(h,s,v)
        self.hue = int(h*65000)
        self.sat = int(s*254)
        self.bri = int(v*254)

    def update(self):
        messagebody = {
            "on": self.on,
            "hue": self.hue,
            "sat": self.sat,
            "bri": self.bri,
            "transitiontime": self.transition_time,
        }
        url = "https://" + self.ip_adress + "/api/" + self.username + \
              "/groups/" + str(self.group_id) + "/action"
        x = requests.put(url, data=json.dumps(messagebody), verify=False)
        return x