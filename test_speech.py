from speak import speak_text

import configuration

config = configuration.get_config()

if __name__ == "__main__":
    text = f'Hello {config["owner"]}'
    speak_text(text)