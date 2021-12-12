from listen import listen_to_microphone

stop_commands = ["quit","exit", "stop listening"]

stop = False 

while not stop:
    speech = listen_to_microphone()
    if speech != None:
        print("speech: "+ speech)
        for command in stop_commands:
            if command in speech:
                stop = True