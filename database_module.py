import sqlite3
import os

os.system("cls")

# To establish connectivity between source code and database
def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

# To store queries into datbase
def get_Ques_Ans():
    connect = create_connection()
    cur = connect.cursor()
    cur.execute('SELECT * FROM questionAndAnswers')

    return cur.fetchall()
       
# To check whether the required query is already in the database or not
def get_ans_from_memory(question):
    
    rows = get_Ques_Ans()
    answer = ''
    
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            # break
            return answer

# To insert data into database
def insert_data(question,answer):
    connect = create_connection()
    cur = connect.cursor()
    data = ""
    
    
    data = "INSERT INTO questionAndAnswers values('"+question+"', '"+answer+"')"
    cur.execute(data)
    connect.commit()

# To fetch assistant's current name
def get_assistant_name():
    connect = create_connection()
    cur = connect.cursor()
    
    data = "select value from assistant_status where name = 'assistant_name'"
    cur.execute(data)
    return cur.fetchall()[0][0]

# To update the assistant's name
def update_assistant_name(new_Name):
    connect = create_connection()
    cur = connect.cursor()
    
    data = "update assistant_status set value = '"+new_Name+"' where name = 'assistant_name'"
    cur.execute(data)
    connect.commit()

# To fetch the last updated date
def get_last_seen():
    connect = create_connection()
    cur = connect.cursor()
    
    data = "select value from assistant_status where name = 'last_seen_date'"
    cur.execute(data)
    return str(cur.fetchall()[0][0])

# To update the date when the JARVIS opened last time in database
def update_last_seen(last_seen_date):
    connect = create_connection()
    cur = connect.cursor()
    
    data = "update assistant_status set value = '"+str(last_seen_date)+"' where name = 'last_seen_date'"
    cur.execute(data)
    connect.commit()

# To turn on the speak function
def speech_on():
    connect = create_connection()
    cur = connect.cursor()
    
    data = "update assistant_status set value ='on' where name = 'speech'"
    cur.execute(data)
    connect.commit()
    return ("OK ! I will speak now. ")

# To turn off the speak function
def speech_off():
    connect = create_connection()
    cur = connect.cursor()
    
    data = "update assistant_status set value ='off' where name = 'speech'"
    cur.execute(data)
    connect.commit()
    return ("OK ! I won't speak. ")


# checking status of speech, to enable/disable the speak function
def check_speak_status():
    connect = create_connection()
    cur = connect.cursor()
    
    data = "select value from assistant_status where name = 'speech'"
    cur.execute(data)
    ans = cur.fetchall()[0][0]

    if ans == 'on':
        return True
    else:
        return False

# To turn on the speaker so that user cangive command verbally
def user_command_on():
    connect = create_connection()
    cur = connect.cursor()
    data = "update user_command_status set status ='on' where command = 'com'"
    cur.execute(data)
    connect.commit()
    return ("You can speak now")

# To turn off the speaker so that user can give command through keyboard
def user_command_off():
    connect = create_connection()
    cur = connect.cursor()
    data = "update user_command_status set status ='off' where command = 'com'"
    cur.execute(data)
    connect.commit()
    return ("You can't speak")

def check_command_status():
    connect = create_connection()
    cur = connect.cursor()
    
    data = "select status from user_command_status where command = 'com'"
    cur.execute(data)
    ans = cur.fetchall()[0][0]
    if ans == 'on':
        return True
    else:
        return False



































# def get_reminder():
#     connect = create_connection()
#     cur = connect.cursor()
#     # INSERT INTO tablename values('question', 'answer')
    
#     data = "select reminder,time from reminderTable"
#     cur.execute(data)
#     return str(cur.fetchall()[0])

# def update_reminder(reminder,time):
#     connect = create_connection()
#     cur = connect.cursor()
    
#     data = "update assistant_status set value = '"+str(last_seen_date)+"' where name = 'last_seen_date'"
#     cur.execute(data)
#     connect.commit()