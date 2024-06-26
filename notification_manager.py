from twilio.rest import Client
from smtplib import SMTP
import os
my_email="YOUR EMAIL"
password="YOUR PASSWORD"
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN =os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER =os.environ.get("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER =os.environ.get("TWILIO_VERIFIED_NUMBER")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self,emails,message):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )


