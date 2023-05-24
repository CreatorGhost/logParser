from smtplib import SMTP_SSL
from email.message import EmailMessage
import json
import pandas as pd
from pretty_html_table import build_table

file = open("config.json")
data = json.load(file)

SENDER_EMAIL = "senderemai@gmail.com"
MAIL_PASSWORD = data["PASSWORD"]
RECEIVER_EMAIL = "reciveremail@gmail.com"

df = pd.read_csv("output.csv")

mail_body = """
Hello welcome to <b>Cyber Creed</b> here is table of content :
{0}

Thanks and Regards
<br>
Aditya Pratap Singh
""".format(build_table(df, "blue_light"))

subject = "Testing mail with our python"


def send_mail(
        SENDER_EMAIL, RECEIVER_EMAIL, MAIL_PASSWORD, subject, mail_body
):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.add_alternative(mail_body, subtype="html")

    with SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, MAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.close()


send_mail(SENDER_EMAIL, RECEIVER_EMAIL, MAIL_PASSWORD, subject, mail_body)
print("Mail Sent")