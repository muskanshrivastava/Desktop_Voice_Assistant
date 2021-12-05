from assistant_details import name
from speak_module import*
from database_module import check_speak_status

def output(out):

    if (check_speak_status()):
        speak(out)
        print()

    else:
        print(name + ' : ',out)
        print() 
