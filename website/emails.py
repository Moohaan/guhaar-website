import sendgrid
import os
from sendgrid.helpers.mail import *

def SendMails(from_email, to_email, subject, content):
    print(os.environ.get('SENDGRID_API_KEY'))
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(from_email)
    to_email = Email(to_email)
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)