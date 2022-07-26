
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailClient():

    BODY_TEMPLATE = "<html><head></head><body> {0} </body></html>"

    ADMIN_INFO_SUBJECT = "New Order for Ushi's Creations"
    CONFIRMATION_SUBJECT = "We Have Received Your Order! - Ushi's Creations"
    CANCELLATION_SUBJECT = "Your Order Has Been Cancelled - Ushi's Creations"
    PAYMENT_SUBJECT = "We Have Received Your Payment! - Ushi's Creations"
    PRODUCTION_SUBJECT = "Your Order Is Ready! - Ushi's Creations!"

    ADMIN_INFO_TEMPLATE = "<p>Hello, </p><br><p>Ushi's Creation has received a \
        new order from {0} {1}. </p>"
    CONFIRMATION_TEMPLATE = "<p>Hello {0},</p><br><p>Thank you for placing an \
            order with Ushi's Creations! Your order confirmation number is \
            {1}. Please keep track of this number and include it in all \
            your messages to us so we can </p>"
    CANCELLATION_PRE_PAY_TEMPLATE = "<p>Hello {0},</p><br><p></p>"
    CANCELLATION_POST_PAY_TEMPLATE = "<p>"
    PAYMENT_PRE_PROD_TEMPLATE = ""
    PAYMENT_POST_PROD_TEMPLATE = ""
    PRODUCTION_PRE_PAY_TEMPLATE = ""
    PRODUCTION_POST_PAY_TEMPLATE = ""


    def __init__(self):

        file = open("./email_module/email_credentials.json", "r")
        credentials = json.load(file)
        file.close()

        self.email = credentials["email"]
        self.mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        self.mail_server.ehlo()
        self.mail_server.starttls()
        self.mail_server.login(self.email , credentials["password"])
    

    def send_customer_order_confirmation(self, id, order):
        recipient = order.email
        subject = EmailClient.CONFIRMATION_SUBJECT
        content = EmailClient.CONFIRMATION_TEMPLATE.format(order.first_name)
        self.__send_email(recipient, subject, content)


    def send_admin_order_info(self, id, order):
        recipient = self.email
        subject = EmailClient.ADMIN_INFO_SUBJECT
        content = EmailClient.ADMIN_INFO_TEMPLATE
        self.__send_email(recipient, subject, content)


    def send_customer_cancellation_confirmation(self, id, order):
        recipient = order.email
        subject = EmailClient.CANCELLATION_SUBJECT
        content = EmailClient.CANCELLATION_TEMPLATE
        self.__send_email(recipient, subject, content)

    def send_customer_payment_confirmation(self, id, order):
        recipient = order.email
        subject = EmailClient.PAYMENT_SUBJECT
        content = EmailClient.PAYMENT_TEMPLATE
        self.__send_email(recipient, subject, content)

    def send_customer_production_completion_confirmation(self, id, order):
        recipient = order.email
        subject = EmailClient.PRODUCTION_SUBJECT
        content = EmailClient.PRODUCTION_TEMPLATE
        self.__send_email(recipient, subject, content)



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
        message.attach(MIMEText(EmailClient.BODY_TEMPLATE.format(content), 'html'))

        self.mail_server.sendmail(self.email, recipient, message.as_string())
