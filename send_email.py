import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


class SendEmail:
    """
    You need to change your gmail settings so that you can be send email from.
    """
    def __init__(self):
        self.send_from = 'sender@exampel.com'
        self.send_to = 'receiver@example.com'
        self.subject = 'I am subject!'

    def send_mail(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['To'] = self.send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.subject

        msg.attach(MIMEText(message))

        gmail_sender = self.send_from
        gmail_passwd = '*****'  # password of your gmail
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(gmail_sender, gmail_passwd)
        smtp.sendmail(self.send_from, self.send_to, msg.as_string())
        smtp.close()

    def main(self):
        message = "Hello!"
        self.send_mail(message)


if __name__ == '__main__':
    SendEmail().main()
