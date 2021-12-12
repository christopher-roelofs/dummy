import json



config_json = open("config.json")
config = json.load(config_json)

actions_json = open("actions.json")
actions = json.load(actions_json)

def get_actions():
    global actions
    return actions

def get_config():
    global config
    return config