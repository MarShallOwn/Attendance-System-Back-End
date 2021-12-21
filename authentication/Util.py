"""
this file used to initialize a class which will 
responsible for sending the email to specific user

"""

from django.core.mail import EmailMultiAlternatives
class Util:
    @staticmethod
    def send_email(data):
        email= EmailMultiAlternatives(
            subject=data['subject'],
            body=data['body'],
            to=[data['to']],
            )
        email.attach_alternative(data['body'],"text/html")
        email.send()