# Automatic-sending-message
Send the message to arrive at a specific time using [twilio](https://www.twilio.com/)

<img src="https://github.com/ruby-kim/Automatic-sending-message/blob/master/images/example.jpeg"  width="50%"/>

* ***master branch***: automatically send messages at a specific time using github action.
* ***local branch***: can test directly in the local environment.

<br><br>

## File Structure
```
.
├─ .github
│  └─ workflows
│     └─ setting.yml
├─ images
│  └─ example.jpeg
│  └─ github secrets.png
├─ .gitignore
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ run.py
└─ student.py
```

<br><br>

## How to use
* ***master branch***:
  * Fork the repository and register github action secrets in the settings
    <img src="https://github.com/ruby-kim/Automatic-sending-message/blob/master/images/github%20secrets.png"  width="50%"/>
  * Set the [.github/workflows/setting.yml](https://github.com/ruby-kim/Automatic-sending-message/blob/master/.github/workflows/setting.yml)
* ***local branch***:
  * Download this repository and install [requirements.txt](./requirements.txt)
    ``` shell
    git clone https://github.com/ruby-kim/Automatic-sending-message.git
    cd Automatic-sending-messsage
    pip3 install -r requirements.txt
    ```
  * create `.env` and set the variables
    ``` .env
    # example
    ACCOUNT_SID="YOUR ACCOUNT SID"
    AUTH_TOKEN="YOUR AUTH TOKEN"

    ONLINE_PHONE_NUMBER = "+12673..."  # your twilio phone number
    MY_PHONE_NUMBER = "+8210..."       # your mobile phone number

    STUDENT_1_NAME=James
    STUDENT_1_DATE_1=Tue
    STUDENT_1_DATE_2=Sat
    STUDENT_1_TIME_1=7 p.m.
    STUDENT_1_TIME_2=10 a.m.
    ```
  * run [run.py](./run.py)
    ``` shell
    python3 run.py
    ```






<br><br>

## Developer
* [@ruby-kim](https://github.com/ruby-kim)
* Email: dev.rubykim@gmail.com   
