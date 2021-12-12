import pyttsx3
import configuration


config = configuration.get_config()

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[config['voice']].id)


def speak_text(text):
    engine.say(text)
    engine.runAndWait()



if __name__ == "__main__":
    pass