""" To send a binary files to a server that is used to work with plain text we 
need to encode the file before transport it

ENCODES BINARY DATA INTO PRINTABLE ASCII CHARACTERES"""

# Sending an email with a PDF file

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = " An email with an attachment file "
body = " This is an email with an attachment sent from Python"
sender_email = "gomezpythonista@gmail.com"
receiver_email = "mairig25@gmail.com"
password = input("Enter your password: ")

# create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email # recommended for mass email

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "test\document.pdf" # in same directory as script

# open pdf file in binary mode
with open(filename, "rb") as attachment:
    # add file as application/octet-stream
    # email client can usually download this authomatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/values pair to attanchment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string 
message.attach(part)
text = message.as_string()

# log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)