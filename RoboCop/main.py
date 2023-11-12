import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.say("Welcome to RoboSpeaker 1.1. I can assist you with reading out anything you would like me to read. Andd just press 'q' if you are bored with me")
    engine.runAndWait()


    print("Welcome to RoboSpeaker 1.1")
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to say (enter 'q' to quit): ")

        if x.lower() == "q":
            break

        engine.say(x)
        engine.runAndWait()