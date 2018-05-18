from time import sleep
import smtplib
import netifaces as ni
import keys
import email.message
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
 

ipHash = str(ni.ifaddresses('wlan0'))
#print ip

ipHashList = ipHash.split(' ')
print ipHashList[11]

ipPlus = ipHashList[11]
ipList = list(ipPlus)
ipList[0] = ""
ipList[-1] = ""
ipList[-2] = ""
ipList[-3] = ""
ipList[-4] = ""
ip = "".join(ipList)

print ip





def doEmail(a,b):   # a = subject, b = message, c = image file name
    # img_data = open(c, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = a
    msg['From'] = keys.emailFrom
    msg['To'] = 'keys.emailTo'
    msg.preamble = "About Cubeputer. The world's most secure computer."
    

    text = MIMEText(b)
    msg.attach(text)
    pic = open('images/cubeputer01.jpg', 'rb')
    img = MIMEImage(pic.read())
    pic.close()
    msg.attach(img)
    
    s = smtplib.SMTP(keys.emailServer, keys.emailPort)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(keys.emailFrom, keys.emailPW)
    s.sendmail(keys.emailFrom, keys.emailTo, msg.as_string())
    s.quit()

doEmail("que", "pllelllease")


