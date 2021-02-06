# import all necessary components
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

PORT = 587  # 2525
SMTP = "smtp.gmail.com"  # "smtp.mailtrap.io"
login = os.environ["email"]  # "e190d3a94a7844"
password = os.environ["pass"]  # "cdba2b9a645bfd"


def send_mail(cmd, recv):
    sender_email = f"Atul Singh <{login}>"
    receiver_email = f"{recv}"
    message = MIMEMultipart("alternative")
    message["Subject"] = "RabbitMq And Python Mailer"
    message["From"] = sender_email
    message["To"] = receiver_email

    # write the HTML part
    html = """\
    <html>
     <head>
      <style>
         .center {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 50%;
                }
         body {
                font-family: Arial;
                margin: 0;
            }
        .header {
                padding: 60px;
                text-align: center;
                background: #1abc9c;
                color: white;
                font-size: 30px;
                }
        .footer {
                padding: 20px;
                text-align: center;
                background: #ff8a00;
                color: white;
                font-size: 20px;
                }
      </style>
     </head>
     <body>
       <div class="header">
            <h1>I am Batman</h1>
        </div>
       <img src="cid:im_attach" class="center">
       <div class="footer">
            <h4>""" + cmd + """</h4>
       </div>
     </body>
    </html>
    """

    print("[mailer] attaching html")
    part = MIMEText(html, "html")
    message.attach(part)

    # We assume that the image file is in the same directory that you run your Python script from
    print("[mailer] loading html image")
    fp = open('batman.png', 'rb')
    image = MIMEImage(fp.read())
    fp.close()

    # Specify the  ID according to the img src in the HTML part
    print("[mailer] attaching image to html")
    image.add_header('Content-ID', '<im_attach>')
    message.attach(image)

    # send your email
    print("[mailer] sending email ... ", end="")
    with smtplib.SMTP(SMTP, PORT) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    print('Sent')

