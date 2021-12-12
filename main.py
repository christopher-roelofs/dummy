import json
from speak import speak_text
from listen import listen_to_microphone
import random
import configuration
from processor import process_command
from time import sleep

config = configuration.get_config()

def replace_token(string):
    return string.replace("{self}",config['self']).replace("{owner}",config["owner"])



while True:
    activate = listen_to_microphone()
    print(activate)
    for phrase in config["activation_phrases"]:
        if activate != "":
            if replace_token(phrase) in activate:
                response = replace_token(random.choice(config["activation_responses"]))
                speak_text(f'{replace_token(response)}')
                command = listen_to_microphone()
                if command != "None":
                    process_command(command)



 