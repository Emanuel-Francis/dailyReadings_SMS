import os
import time
from twilio.rest import Client
from daily_readings import send

account_sid = os.environ.get('account_sid')
print(account_sid)
auth_token = os.environ.get('auth_token')
message = send()


client = Client(account_sid, auth_token)
client.messages.create(
            to= "SEND_NUMBER",
            from_="FROM_NUMBER",
            body = message
        )

start_time = time.time()
alarm = 43200
print("Bible Study Notification via SMS started: " + start_time)
while True:
    current_time = time.time()
    pass_time = current_time - start_time
    print("Sending in:" + pass_time)

    if pass_time > alarm:
        print("Sent")
        client.messages.create(
            to= "SEND_NUMBER",
            from_="FROM_NUMBER",
            body = message
        )

