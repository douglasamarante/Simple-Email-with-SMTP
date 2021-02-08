import smtplib

import config

def send_email(subject, msg):
    try:
        #the server that this code is using are outlook
        server = smtplib.SMTP('smtp-mail.outlook.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.EMAIL_PASS)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_TEST, message)
        server.quit()
        print("Email sending has been completed")
    except:
        print("Email sending failed")

subject = input("Type the email subject: ")
msg = input("Type the body message: ")

send_email(subject, msg)
