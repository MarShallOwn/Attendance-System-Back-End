"""
this file used to initialize a class which will 
responsible for sending the email to specific user

"""

from django.core.mail import EmailMessage
class Util:
    @staticmethod
    def send_email(data):
        email= EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=[data['to']],
            )
        email.send()