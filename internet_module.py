import urllib.request
import webbrowser
import yagmail
from input_module import take_input
from wikipedia import summary
import pywhatkit

def check_internet_connection():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False

def check_youtube():
    try:
        yt = webbrowser.open('youtube.com')
        return yt
    except :
        return "None"

def check_facebook():
    try:
        yt = webbrowser.open('facebook.com')
        return yt
    except :
        return "None"

def gmail(reciever, message, sender, subject):
    try:
        sender_gmail = yagmail.SMTP(sender)
        sender_gmail.send(to = reciever, subject = subject, contents = message)
        return True
    except:
        return False

def wikipedia(query):
    query.lower()
    query = query.replace("tell me about","")
    query = query.replace("who is","")
    query = query.replace("what is","")
    query = query.replace("how can we","")
    query = query.replace("can you","")
    query.strip()
    try:
        results = summary(query, sentences=2)
        #print(results)
        return results
    except Exception as e:
        return ""

def play_music(music):
    pywhatkit.playonyt(music)
    try:
        return True
    except:
        return False


def get_news():
    try:
        webbrowser.open('https://news.google.com/')
        return True
    except:
        return False
