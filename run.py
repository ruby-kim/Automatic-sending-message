import os
from dotenv import load_dotenv
from twilio.rest import Client
from student import *


def generate_body(time, name):
    return f'''\n\nYou have a class at {time} for {name} today.\nPlease prepare it in advance.'''


def send_sms(student, idx):
    message = client.messages.create( 
        from_=os.getenv('ONLINE_PHONE_NUMBER'),  
        body=generate_body(student.time[idx], student.name),      
        to=os.getenv('MY_PHONE_NUMBER')
    )
    try:
        message.sid
        print("Sending the message successfully")
    except:
        print("Error!")


if __name__ == "__main__":
    load_dotenv(verbose=True)
    account_sid = os.getenv('ACCOOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    students = [Student1(), Student2()]

    for student in students:
        for idx, day in enumerate(student.days):
            if validate_days(day):
                send_sms(student, idx)
                break
