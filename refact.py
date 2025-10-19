import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def send_message(self, recipients: list, subject: str, message: str):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        # Создаем соединение и закрываем его после отправки
        with smtplib.SMTP(self.GMAIL_SMTP, 587) as ms:
            ms.ehlo()
            ms.starttls()
            ms.ehlo()
            ms.login(self.login, self.password)
            ms.sendmail(self.login, recipients, msg.as_string())

    def receive(self, header=None):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = f'(HEADER Subject "{header}")' if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        if not data[0]:
            mail.logout()
            raise ValueError('There are no letters with current header')
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    l = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    email_client = Email(l, password)
    email_client.send_message(recipients, subject, message)
    
    try:
        email_msg = email_client.receive(header)
        print(f'Получено письмо с темой: {email_msg["Subject"]}')
    except ValueError as err:
        print(err)