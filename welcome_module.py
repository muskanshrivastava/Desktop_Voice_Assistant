from time_module import get_hours, get_date
from output_module import output
from database_module import update_last_seen, get_last_seen
from datetime import date
from speak_module import*


def greet():
    
    #fetching previous date
    previous_date = get_last_seen() 
   

    #fetching today's date
    today_date = get_date()
    update_last_seen(today_date)

    if previous_date == today_date:
        speak("Welcome Back !")

    else:
        
        hour = int(get_hours())
        
        if hour>=0 and hour<12:
            speak("Good Morning!")
            

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
            

        else:
            speak("Good Evening!")