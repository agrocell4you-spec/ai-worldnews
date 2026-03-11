import smtplib
from email.mime.text import MIMEText

BLOG_EMAIL="agrocell4you.seed5626A@blogger.com"

SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587

EMAIL="YOUR_GMAIL"
PASSWORD="APP_PASSWORD"


def post_to_blogger(title,content):

    msg=MIMEText(content,"html")
    msg["Subject"]=title
    msg["From"]=EMAIL
    msg["To"]=BLOG_EMAIL

    server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
    server.starttls()
    server.login(EMAIL,PASSWORD)

    server.sendmail(EMAIL,BLOG_EMAIL,msg.as_string())

    server.quit()