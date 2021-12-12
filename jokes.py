import requests
import json
from speak import speak_text




def get_joke_of_day():
    response = requests.get("https://api.jokes.one/jod")
    if response.status_code != 200:
        return json.loads(response.text)["error"]["message"]
    else:
        return(json.loads(response.text)["contents"]["jokes"][0]["joke"]["text"])

def get_norris_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return json.loads(response.text)["value"]

def process_command(command):
    if "norris" in command or "chuck norris" in command or "chuck" in command:
        joke = get_norris_joke()
        speak_text(joke)
    if "of the day" in command:
        joke = get_joke_of_day()
        speak_text(joke)


if __name__ == "__main__":
    print(get_norris_joke())