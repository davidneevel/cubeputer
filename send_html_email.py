#check email stuff
import imaplib
imapMail = imaplib.IMAP4_SSL('imap.gmail.com')


#Compose and send email stuff
import cgi
import uuid
import keys
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText
from email.mime.image     import MIMEImage
from email.header         import Header
import os
import smtplib
from email.MIMEBase import MIMEBase
from email import Encoders

# GPIO stuff
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
solenoidPin = 40
GPIO.setup(solenoidPin, GPIO.OUT)


gmail_user = keys.emailFrom
gmail_pwd = keys.emailPW
email_to = keys.emailTo

def attach_image(img_dict):
    with open(img_dict['path'], 'rb') as file:
        msg_image = MIMEImage(file.read(), name = os.path.basename(img_dict['path']))
        msg_image.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
        return msg_image


def generate_email(gmail_user, to_list):
    msg =MIMEMultipart('related')
    msg['Subject'] = Header(u'Information about CUBEPUTER, the world\'s most secure computer', 'utf-8')
    msg['From'] = gmail_user
    msg['To'] = ','.join(to_list)
    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(u'Image not working - maybe next time', 'plain', 'utf-8')
    msg_alternative.attach(msg_text)
    msg.attach(msg_alternative)
    msg_html = u'<h1>CUBEPUTER</h1>'

    msg_html += u'<h3>CUBEPUTER</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img13['title'], quote=True), **img13)
    msg_html += u'CUBEPUTER is a computer completely encased in concrete for ultimate secuity. No wires in or out. No physical connection to the outside world. What could be more secure? It is waterproof, perhaps even hammerproof. Here is some information on the building of Cubeputer:\n'

    msg_html += u'<h3>Testing the circuit</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img1['title'], quote=True), **img1)
    msg_html += u'The first step was to get all the components together and make sure the Rapsberry Pi would get enough power from a wireless charger. Here is the wireless charger, wireless receiver, battery charger, battery and Raspberry Pi Zero all plugged in and running.\n'
    
    msg_html += u'<h3>Testing the wireless charging</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img5['title'], quote=True), **img5)
    msg_html += u'The next step was to make sure the wireless charger would deliver enough power through a layer of concrete. This was the step I was most concerned about because the whole project relied on this working. It worked fine.\n'

    msg_html += u'<h3>Laser cut and assembled concrete forms</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img3['title'], quote=True), **img3)
    msg_html += u'This is what the forms looked like for the botom half of the concrete cube. The only tricky thing was to make them in a way that would keep the bottom layer of concrete thin enough to allow wireless charging.\n'

    msg_html += u'<h3>Designing concrete forms</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img2['title'], quote=True), **img2)
    msg_html += u'And this is what desigining the forms looks like in Fusion 360.\n'


    msg_html += u'<h3>3d printed internal structure</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img8['title'], quote=True), **img8)
    msg_html += u'Inside the concrete, the electronics are arranged in a 3d printed structure. The Rasperry Pi mounts to the inside of the shaped bit on the left, which makes up the inside of the top of the concrete form. By this stage I had also decided to add another electric component- a small solenoid, visible at the lower left of the electronics bit. This is arranged so it can tap on the inside of the concrete box, the computer\'s one non electronic way of communicating with the outside.\n'


    msg_html += u'<h3>Ready for the top layer of concrete</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img11['title'], quote=True), **img11)
  
    msg_html += u'<h3>Voila.</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img12['title'], quote=True), **img12)
    msg_html += u'This is what it looks like sitting on my desk.\n'

    msg_html += u'<h3>Coding</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img15['title'], quote=True), **img15)
    msg_html += u'The final step was to program it to send out this email to you in response to your email.\n'


    msg_html += u'<h3>CUBEPUTER</h3><div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(alt=cgi.escape(img13['title'], quote=True), **img13)
    msg_html += u'CUBEPUTER thanks you for your interest in CUBEPUTER.\n'



    msg_html = MIMEText(msg_html, 'html', 'utf-8')
    msg_alternative.attach(msg_html)
    msg.attach(attach_image(img1))
    msg.attach(attach_image(img2))
    msg.attach(attach_image(img3))
    msg.attach(attach_image(img5))
    msg.attach(attach_image(img8))
    msg.attach(attach_image(img11))
    msg.attach(attach_image(img12))
    msg.attach(attach_image(img13))
    msg.attach(attach_image(img15))
    
    return msg
    print "email generated"

def solenoid():
    GPIO.setup(solenoidPin, GPIO.OUT)
    GPIO.output(solenoidPin, GPIO.HIGH)
    sleep(.25)
    GPIO.output(solenoidPin, GPIO.LOW)
    GPIO.cleanup()

def send_email(msg, gmail_user, gmail_pwd, to_list):
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to_list, msg.as_string())
    mailServer.quit()
    print "email sent"

img1 = dict(title = 'Testing the circuit', path = '/python/cubeputer/images/cubeputer01.jpg', cid = str(uuid.uuid4()))

img2 = dict(title = 'Designing concrete forms', path = '/python/cubeputer/images/cubeputer02.jpg', cid = str(uuid.uuid4()))

img3 = dict(title = 'Assembled, laser cut concrete form', path = '/python/cubeputer/images/cubeputer03.jpg', cid = str(uuid.uuid4()))
# image 4 not used! it's ugly!
img5 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer05.jpg', cid = str(uuid.uuid4()))
img8 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer08.jpg', cid = str(uuid.uuid4()))
img10 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer10.jpg', cid = str(uuid.uuid4()))
img11 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer11.jpg', cid = str(uuid.uuid4()))
img12 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer12.jpg', cid = str(uuid.uuid4()))
img13 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer13.jpg', cid = str(uuid.uuid4()))
img15 = dict(title = 'Wireless charging test', path = '/python/cubeputer/images/cubeputer15.jpg', cid = str(uuid.uuid4()))




if __name__ == "__main__":
    email_msg = generate_email(gmail_user, [email_to])
    send_email(email_msg, gmail_user, gmail_pwd, [email_to])
    solenoid()