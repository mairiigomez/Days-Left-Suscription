"""Configuring our email and sending a plain text to the receiver
We create a secure connection with SMTP_SSL and have to use the port 465"""

import smtplib, ssl

port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "gomezpythonista@gmail.com"
receiver_email = "mairig25@gmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent by Python."""

# create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
