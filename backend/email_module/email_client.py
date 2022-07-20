
import json
import smtplib, ssl

class EmailClient():

    file = open("./email_module/email_credentials.json")
    credentials = json.load(file)

    PORT = credentials["smtp_ssl_required_port"]
    SMTP_SERVER_DOMAIN_NAME = credentials["smtp_server"]
    SENDER_MAIL = credentials["email"]
    SENDER_PASSWORD = credentials["password"]
    
    
    @classmethod
    def send(cls):
        emails = ["sahir.mody@gmail.com"]
        subject = "test"
        content = "test"


        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(cls.SMTP_SERVER_DOMAIN_NAME, cls.PORT, context=ssl_context)
        service.login(cls.SENDER_MAIL, cls.SENDER_PASSWORD)
        
        for email in emails:
            result = service.sendmail(cls.SENDER_MAIL, email, f"Subject: {subject}\n{content}")

        service.quit()
