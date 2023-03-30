import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self):
        self.login = "login@gmail.com"
        self.password = "qwerty"
        self.subject = "Subject"
        self.recipients = ["vasya@email.com", "petya@email.com"]
        self.message = "Message"
        self.header = None

    def send_message(self):
        msg = MIMEMultipart()
        msg["From"] = self.login
        msg["To"] = ", ".join(self.recipients)
        msg["Subject"] = self.subject
        msg.attach(MIMEText(self.message))

        server = smtplib.SMTP(self.GMAIL_SMTP, 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.login, self.password)
        server.sendmail(self.login, server, msg.as_string())
        server.quit()

        return print("successfully sent email to %s:" % (msg["To"]))

    def recieve(self):
        imap = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        imap.login(self.login, self.password)
        imap.list()
        imap.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else "ALL"
        result, data = imap.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = imap.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        imap.logout()

        return email_message


if __name__ == "__main__":
    mail = Email()
    mail.send_message()
    mail.recieve()
