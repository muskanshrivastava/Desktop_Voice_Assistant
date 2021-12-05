import pyttsx3
import pywhatkit
from speech_recognition import Microphone, Recognizer, UnknownValueError, RequestError
import datetime
import wikipedia
import webbrowser
import os
import win10toast
import cv2
from plyer import notification





engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    print("Jarvis: ",audio)
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")      

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takecommand():
    recog = Recognizer()
    mic = Microphone()

    with mic:
        recog.adjust_for_ambient_noise(mic, duration=1)

        print("Listening...")
        audio = recog.record(mic, 4)

    try:
        recognized = recog.recognize_google(audio)    
        print("You said: ",recognized)

    except RequestError as exc:
        print(exc)

    except Exception as e:
        print("Say again Please: ")
        return "None"  
   
    return recognized

def notifyMe(note):
    notification.notify(
        title = "notification",
        message = note,
        timeout=120  
        )
    speak(note)

if __name__ == "__main__":
    os.system("cls")
    wishMe()
    while True:
        recognized = takecommand().lower()


        if 'wikipedia' in recognized:
            speak('Searching Wikipedia...')
            recognized = recognized.replace("wikipedia", "")
            results = wikipedia.summary(recognized, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in recognized:
           webbrowser.open('youtube.com')

        elif 'whatsapp' in recognized:
            speak('What message should i send.')
            msg = takecommand()
            pywhatkit.sendwhatmsg(f"+91{8962991655}", msg ,20,58)

        elif 'open google' in recognized:
            webbrowser.open('google.com')

        elif 'stackoverflow' in recognized:
            webbrowser.open('stackoverflow.com')

        elif 'time' in recognized:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open code' in recognized:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
    
        elif 'send email' in recognized:
            pywhatkit.send_mail("choudharymanu514@gmail.com","M@nu0129","jarvis","this is mail",
            "meroolchoudhary2000@gmail.com")

        elif 'play' in recognized:
            recognized = recognized.replace("play","")
            pywhatkit.playonyt(recognized)
   
        elif 'news' in recognized:
            webbrowser.open('Google News')  

        elif 'camera' in recognized:
            camera = cv2.VideoCapture(0)
            i=0
            while i < 1:
    
                input('press Enter to capture')
                return_value, image = camera.read()
                cv2.imwrite('opencv'+str(i)+'.png', image)
                i+=1
            del(camera) 

        elif 'remind me' in recognized:
            speak("What would i remind you sir")
            # rememberMsg = recognized.replace("remind me","")                
            # rememberMsg = rememberMsg.replace("Jarvis","")
            note = takecommand()
            remember = open('data.txt','w')
            remember.write(note)
            remember.close()
            speak("Ok I will notify you")
            time.sleep(120)
            notifyMe(note)
           
        elif 'what do you remember' in recognized:
            remember = open('data.txt','r')
            speak("You told me that" + remember.read())  

        elif 'quit' in recognized:
            quit()        