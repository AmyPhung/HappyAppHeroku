"""The first step is to create an SMTP object, each object is used for connection
with one server."""

#TODO: Add key for email/password so it's not online
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendEmailTo(to):
    """
    This function sends a wholesome email to the specified "to_email"
    Input:
    to - (string), the email address you would like to send to ]
    Returns:
    None
    """
    try:
        ImgFileName = "good_boi.png"
        img_data = open(ImgFileName, 'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = 'I heard you were feeling down...'
        msg['From'] = 'happybot184@yahoo.com'
        msg['To'] = to
        text = MIMEText("So I'm sending you this cute picture to cheer you up!")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('beehappytest1@gmail.com','b33h@ppy')
        s.sendmail('beehappytest1@gmail.com',to,msg.as_string())
        s.quit()
        return True
    except:
        return False
    # gmail_user = 'beehappytest1@gmail.com'
    # gmail_password = 'b33h@ppy'
    #
    # sent_from = gmail_user
    # subject = "Happy"
    # body = "Hey, what's up?"
    #
    #
    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s
    #
    # %s
    # """ % (sent_from, ", ".join(to), subject, body)
    #
    # email_text = "asdf"
    #
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login(gmail_user, gmail_password)
    # server.sendmail(sent_from, to, email_text)
    # server.close()

if __name__ == "__main__":
    sendEmailTo("epan547@gmail.com")
