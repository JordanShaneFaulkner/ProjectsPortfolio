#Jordan Faulkner 5-18-2024
#In this project, I will create a function that will send emails for me using this Python script

import smtplib
from email.mime.text import MIMEText
APP_PASSWORD = '****************'
subject = 'Test email'
body = 'Hello, This is a test email sent from a Python script. I wrote a program that automates sending emails without opening any browsers.'
sender = 'jordan.developermail@gmail.com'
recipients = [sender,'jordanshanefaulkner@gmail.com','tmckenna@broadinstitute.org']

def send_email(subject,body,sender,recipients,password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(sender,APP_PASSWORD)
        smtp_server.sendmail(sender,recipients,msg.as_string())
        print('Message sent!')

send_email(subject,body,sender,recipients,APP_PASSWORD) 
