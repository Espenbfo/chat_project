import requests

url = "http://localhost:5000"
greet_response = requests.get(url + "/greet")
print("uuid", greet_response.json())

with open("audio.m4a", "rb") as f:
    response = requests.post(url + "/speak", data={"id": greet_response.json()["id"]},
                             files={"file": f})
    print(response.json())

with open("step2.m4a", "rb") as f:
    response = requests.post(url + "/speak", data={"id": greet_response.json()["id"]},
                             files={"file": f})
    print(response.json())