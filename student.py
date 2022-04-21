import os
from dotenv import load_dotenv
from twilio.rest import Client
import datetime
from pytz import timezone


def get_days(year, month, day):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return days[datetime.date(year, month, day).weekday()]


def validate_days(days):
    current_time = datetime.datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
    year, month, day = map(int, current_time.split()[0].split('-'))
    if get_days(year, month, day) in days:
        return True
    return False


class Student1:
    def __init__(self) -> None:
        load_dotenv(verbose=True)
        self.name = os.getenv('STUDENT_1_NAME')
        self.days = [os.getenv('STUDENT_1_DATE_1'), os.getenv('STUDENT_1_DATE_2')]
        self.time = [os.getenv('STUDENT_1_TIME_1'), os.getenv('STUDENT_1_TIME_2')]


class Student2:
    def __init__(self) -> None:
        load_dotenv(verbose=True)
        self.name = os.getenv('STUDENT_2_NAME')
        self.days = [os.getenv('STUDENT_2_DATE_1')]
        self.time = [os.getenv('STUDENT_2_TIME_1')]
