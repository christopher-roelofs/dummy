import speech_recognition as sr

def listen_to_microphone():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=.5)
        # r.energy_threshold()
        while True:
            try:
                print("Listening for command...")
                audio= r.listen(source)
                text = r.recognize_google(audio)
                return(text.lower())
            except Exception as e:
                return("")



if __name__ == "__main__":
    pass