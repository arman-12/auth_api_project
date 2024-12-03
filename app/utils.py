import re
from flask_mail import Message

def validate_email_format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_verification_email(email, mail):
    msg = Message('Verification Email', sender='ahossain3324@gmail.com', recipients=[email])
    msg.body = 'Please verify your email address by clicking the link below.'
    mail.send(msg)
