from speech_recognition import Microphone, Recognizer, UnknownValueError, RequestError
import pyttsx3
import input_module
# from output_module import*
from assistant_details import name

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)


def speak(audio):
    print(name,": ", audio)
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    recog = Recognizer()
    mic = Microphone()

    with mic:
        recog.adjust_for_ambient_noise(mic, duration=1)

        print("Listening...")
        audio = recog.record(mic, 4)

    try:
        recognized = recog.recognize_google(audio)    
        print("User : ",recognized)

    except RequestError as exc:
        print(exc)

    except Exception as i:
        i = input("Me : ")
        return i

    return recognized 


# print(voices)
# print(voices[1].id)