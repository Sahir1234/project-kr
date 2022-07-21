
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailClient():

    file = open("./email_module/email_credentials.json")
    credentials = json.load(file)

    PORT = credentials["smtp_ssl_required_port"]
    SMTP_SERVER_DOMAIN_NAME = credentials["smtp_server"]
    EMAIL = credentials["email"] 
    PASSWORD = credentials["password"]

    sampel_content = """\
            <html>
            <head></head>
            <body>
                <p>Hi!<br>
                How are you?<br>
                Here is the <a href="http://www.python.org">link</a> you wanted.
                </p>
            </body>
            </html>
            """
    
    @classmethod
    def send_order_confirmation_to_customer(cls, customer, subject, content):
        pass

    @classmethod
    def send_order_confirmation_to_manufacturer(cls, subject, content):
        pass
    
    @classmethod
    def __send_email(cls, recipient, subject, content):
        """
        Sends an email to the recipient from the email in credentials.json

        The content argument should be a string containing a properly formatted html
        document that is the body of the email.
        """

        message = MIMEMultipart('alternative')
        message['From'] = cls.EMAIL
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(content, 'html'))

        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.login(cls.EMAIL, cls.PASSWORD)
        mail_server.sendmail(cls.EMAIL, recipient, message.as_string())
        mail_server.quit()
