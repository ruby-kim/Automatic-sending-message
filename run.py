import os
from twilio.rest import Client
from student import *


def generate_body(time, name):
    """ generate message
    time: str  -> ex) 7 p.m.
    name: str  -> ex) James
    
    return day of the week
    """
    return f'''\n\nYou have a class at {time} for {name} today.\nPlease prepare it in advance.'''


def send_sms(student, idx):
    """ send sms based on settings
    student: class object
    idx: int  -> ex) 1
    
    return None
    """
    message = client.messages.create( 
        from_=os.environ['ONLINE_PHONE_NUMBER'],  
        body=generate_body(student.time[idx], student.name),      
        to=os.environ['MY_PHONE_NUMBER']
    )
    try:
        message.sid
        print("Sending the message successfully")
    except:
        print("Error!")


if __name__ == "__main__":
    account_sid = os.environ['ACCOOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    students = [Student1(), Student2()]

    for student in students:
        for idx, day in enumerate(student.days):
            if validate_days(day):
                send_sms(student, idx)
                break
