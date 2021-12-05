from input_module import take_input
from output_module import output
from os import system
from process_module import process
from welcome_module import greet
# from speak_module import*
# from database_module import check_command_status

system('cls')
greet()
while True:
    try:
        i = take_input()
        out =  process(i)
        output(out)
        # break
    except: 
        print("INVALID INPUT.... RESTART THE PROGRAM !")
        exit()
    
        
   
    