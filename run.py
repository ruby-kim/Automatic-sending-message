import os
import dotenv import load_dotenv
from twilio.rest import Client

if __name__ == "__main__":
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create( 
                from_='',  
                body='''I have a class at 6 p.m. today.
                        Please prepare it in advance.''',      
                to='' 
    ) 
    
    print(message.sid)