from time_module import *
from database_module import *
from input_module import take_input
from output_module import output
from internet_module import *
from assistant_details import name
from speak_module import*


def process(query):
    
    # answer = takeCommand().lower()
    answer =  get_ans_from_memory(query)
    
    # COnditions for accessing applications           
    if answer == "get time details":
        return get_time(query)

    if answer == "code":
        if os.system('start code') == 0:
            return 'opening...'

    elif answer == "play":
        if play_music(query):
            return "Playing..."

    elif answer == "open news":
        if get_news():
            return "opening...."
        else:
            return "Can't fetch right now"
            
    elif answer == "date details":
        return str(get_date())

    elif answer == "check internet connection":
        if check_internet_connection():
            return "Internet is connected"
        else:
            return "Internet is not connected"

    elif answer == "open youtube":
        if check_youtube():
            return "OK" 
        else:
            return "Can't open youtube. Please check internet connectivity"

    elif answer == "open facebook":
        if check_facebook():
            return "OK"
        else:
            return "Can't open facebook. Please check internet connectivity" 
    
    elif  answer in "tell me about":
        answer = answer.replace("tell me about","")
        answer = answer.strip()
        print(answer)
        result = wikipedia(answer)
        return  result

    elif answer == "open gmail":
        if webbrowser.open('gmail.com'):
            return 'opening...'

    elif answer == "open email":
        output("Enter reciever's email")
        # print()
        reciever  = take_input()
        output("Enter sender's email")
        # print() 
        sender = take_input() 
        output("Enter subject of the mail")
        # print()
        subject = take_input() 
        output("What message should I send ?")
        # print()
        message = take_input() 
       
        if gmail(reciever, message, sender, subject):
            return "Mail Sent successfully !!"
        else:
            return "Sorry... mail has not sent"
        
    elif answer == "change name":
        output("OK ! what would you want to call me")
        new_Name = take_input()
        if new_Name == get_assistant_name():
            return "Its just my current name"
        else:
            update_assistant_name(new_Name)
            name = new_Name
            return "Now you can call me "+ new_Name + " :) !!"

    elif answer == "on speak":
       return speech_on()

    elif answer == "off speak":
       return speech_off()

    elif answer == "verbal on":
        return user_command_on()

    elif answer == "verbal off":
        return user_command_off()
        
    elif answer in ["quit", "exit"] :
        output("Thank You !! :) ")
        exit()
    
    else:
        output("I didn't get this one. Should I search on Wikipedia")
        option = take_input()

        if option.lower() in ['yes','Yes', 'YES','y','Y']:
            answer =  wikipedia(query)
            if answer != "":
                return answer
            else :
                return "Can't find results" 

        else:

            output("Can you please tell me what it means ?")
            ans = take_input()
            
            if "it means" in ans:
                ans = ans.replace("it means","")
                ans = ans.strip()
                    
                value = get_ans_from_memory(ans)
            if value == "":
                return "Can't get this one"
            else:
                insert_data(query,value)
                return "THANKS! I will remember it for the next time"  










        # elif answer == "None":
        # output("What sould you I remind you sir")
        # msg = take_input()
        # message,time = input_reminder(msg)
        
        # update_reminder(message,time)
        # return "OK! I will notify you"
        # if get_reminder()[1] == datetime.datetime.now():
        #     return show_reminder(message)
            