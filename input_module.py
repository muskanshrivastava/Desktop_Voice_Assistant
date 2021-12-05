from database_module import check_command_status
from speak_module import takeCommand
def take_input():
    if check_command_status():
        i =  takeCommand()
        print()
        return i
    else:
        
        i = input("me : ")
        print()
        return i
       