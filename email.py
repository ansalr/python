import smtplib

sender = 'ansal_r@outlook.com.com'
receivers = ['robinsonresa3005@gmail.com.com']
message = """From: From Person <from@example.com>
To: To Person <to@example.com>
Subject: SMTP email example


This is a test message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
except SMTPException:
    pass