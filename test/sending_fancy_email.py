"""To send an HTML email, the receiver have the option to render plain text o HTML 
So both option are going to be combined"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "gomezpythonista@gmail.com"
receiver_email = "mairig25@gmail.com"
password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

#create the plain-text and HTML version of your message
text = """\
Hi, 
I hope this email finds yo well"""
html = """\
<html>
  <body>
    <p> Hi, <br>
      How are you?<br>
      <a href="https://journal-as-you-learn.herokuapp.com/"> link </a>
      check it out
    </p>
  </body>
</html>
"""
# turn into plain/hmtl MIMEtext objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# add plain/html to MIMEmultipart message
# the email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# create secure conection with server and send email
context  = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
