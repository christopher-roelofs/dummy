import jokes
import configuration
import sys

actions = configuration.get_actions()
subscriptions = configuration.get_config()["subscriptions"]
action_threashold = .8

def process_command(command):
    print(command)
    for speech in actions:
        tokenized = speech.split()
        total = 0
        for token in tokenized:
            if token in command:
                total += 1
        positivity = total/(len(tokenized))
        if positivity >= action_threashold:
            print(f'Action match positivity: {positivity} for "{command}"')
            action = actions[speech]["action"]
            if action in subscriptions:
                if action == "joke":
                    jokes.process_command(command)
                if action == "stop":
                    sys.exit()
                break

if __name__ == "__main__":
    for speech in actions:
        print(speech)