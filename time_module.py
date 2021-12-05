from database_module import *
from output_module import output
import re
import time
from plyer import notification
from datetime import datetime, date


def get_time(query):

    time = get_ans_from_memory(query)
    if time == 'get time details':
        time = datetime.now().strftime("%I:%M:%S")
        
        return time
    
def get_hours():
    return (datetime.now().strftime("%I"))

def get_date():
    return str(date.today())




# def input_reminder(answer):
#     # to extract time from the answer. findall() returns list of digits
    
#     time = re.findall(r'\d+',answer)
#     time = str(time[0])
#     #print(time)
#     # to extract reminder from answer
#     answer = answer.replace("remind me", "")
#     answer = answer.replace("jarvis", "")
#     answer = answer.replace("I have a", "")
#     answer = answer.replace("at", "")           # i have a meeting tommorow at 7 am
#     answer = answer.replace("am", "")
#     answer = answer.replace("pm", "")
#     answer = answer.replace(time, "")
#     answer = answer.strip()
#     #print(answer,time)
#     return answer,time
    

# def show_reminder(msg):
#     notification.notify(
#         title = "notification",
#         message = msg,
#         timeout=120  
#         )
#     time.sleep(1)