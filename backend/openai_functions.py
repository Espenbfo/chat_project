import re

import openai
from dotenv import load_dotenv
import os
import light_group

load_dotenv()
openai.api_key = os.environ.get('OPENAI_TOKEN')
ROOMS_TO_LIGHT_GROUP={"Espens bedroom": 3, "Living room": 2}
ROOMS = list(ROOMS_TO_LIGHT_GROUP.keys())
rooms_aug = {', '.join(map(lambda x: '"' + x + '"',ROOMS))}
CONTEXT = f"You are a helpful AI Assistant. If the user asks to change the light, reply: \"Changing the lights in ROOM to COLOR\", where COLOR is specified in hex code and ROOM is one of ({rooms_aug}). You must choose of one these rooms, and always use the full name. It is important that you specify the color in hex code. If the color is unclear, do your best to find a fitting color. If asked anything else, do your best to help.\n\n"

def respond(new_query: str, log: list):
    context = CONTEXT
    bot_name="AI Assistant"
    user_name = "User"
    string_log = ""
    for query, response in log:
        string_log += f"{user_name}:{query}\n\n{bot_name}:{response}\n\n"
    # successful
    prompt = f"{context}{string_log}John: {new_query}\n\n{bot_name}:"
    print(prompt)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0,
        stop=["\n\n"],
    )
    best_response = response["choices"][0]["text"]
    extract_command(best_response)
    return response["choices"][0]["text"]

def extract_command(response: str):
    response = response.lower()
    if "changing the lights" in response:
        selected_room = None
        color = None
        for room in ROOMS:
            if room.lower() in response.replace("'", ""):
                selected_room = room
                break
        color_query = re.findall(r"#\w+", response)
        if len(color_query):
            color = color_query[0]
        print(f"Changing the lights in {selected_room} to {color}")
        if selected_room is not None and color is not None:
            print(f"Changing the lights in {selected_room} to {color}")
            room_key = ROOMS_TO_LIGHT_GROUP[selected_room]
            light_group_instance = light_group.LightGroup(room_key)
            light_group_instance.update_values(True, color)
            light_group_instance.update()
        return
    print("No command")