import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SETTINGS

def load_excel(sheet_name):
    return pd.read_excel('test_cases.xlsx', sheet_name=sheet_name)

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SETTINGS["sender_email"]
    msg['To'] = ', '.join(EMAIL_SETTINGS["recipient_emails"])
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(EMAIL_SETTINGS["smtp_server"], EMAIL_SETTINGS["port"]) as server:
        server.starttls()
        server.login(EMAIL_SETTINGS["sender_email"], EMAIL_SETTINGS["password"])
        server.sendmail(msg['From'], EMAIL_SETTINGS["recipient_emails"], msg.as_string())