import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.environ.get('OPENAI_TOKEN')


def respond(query: str, log: list):
    bot_name="Peter Strandwich"
    user_name = "John"
    string_log = ""
    for query, response in log:
        string_log += f"{user_name}:{query}\n\n{bot_name}:{response}\n\n"
    # successful
    prompt = f"{bot_name} er en framtredende komiker. Dette er samtalen som gjorde han kjent på internettet.\n\n{string_log}John: {query}\n\n{bot_name}:"

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0,
        stop=["\n\n"],
    )
    return response["choices"][0]["text"]