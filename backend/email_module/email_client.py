
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailClient():

    def __init__(self):

        file = open("./email_module/email_credentials.json")
        credentials = json.load(file)

        self.email = credentials["email"]
        self.mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        self.mail_server.ehlo()
        self.mail_server.starttls()
        self.mail_server.login(self.email , credentials["password"])

        self.body_template = "<html><head></head><body> {0} </body></html>"

    
    #def customer_contact(self, )


    def __send_email(self, recipient, subject, content):
        """
        Sends an email to the recipient from the email in credentials.json

        The content argument should be a string containing a properly formatted html
        body that is the body of the email.
        """

        message = MIMEMultipart('alternative')
        message['From'] = self.email
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(self.body_template.format(content), 'html'))

        self.mail_server.sendmail(self.email, recipient, message.as_string())
