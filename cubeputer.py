''' this one is meant to be run with a cron scheduler
edit  cron jobs with "crontab -e"
the file "cubeputer_loop" is the same thing but uses a while loop instead of cron
'''



import imaplib
import time
from time import sleep
from time import time
import send_html_email as send



# check last checked list stuff
import os
last = eval(open("/python/cubeputer/last_email_checked.txt").read())   # need absolute address to run correctly with crontab
print "last email checked was %r" % last

def update_list(a):   # updates the text file with the latest checked email number in it
    update = str(a)
    write_to = open('/python/cubeputer/last_email_checked.txt', 'w')
    write_to.write(a)
    write_to.close()

import sys                  # need this to add a place to look for files
import keys
         # parent directory.

fromEmail = keys.emailFrom
password = keys.emailPW

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(fromEmail,password)
mail.list()




cycles = 0
errors = 0


try:
    mail.select("inbox")

    result, data = mail.search(None, "ALL")

    ids = data[0]  # data is a list
    id_list = ids.split()  # ids is a space separated string
    latest_email_id = id_list[-1]  # get the latest


    print "last = %d" % last


    print "latest = %s" % (latest_email_id)
    # t = time.ctime()
    # print " checked at %s" % t,
    print " Cycles: %d" % cycles,
    print " Errors: %d" % errors

    if int(latest_email_id) != last:
        print "doesn't equal last"
        emails_to_do = int(latest_email_id) - last
        print "got %d emails to do" % emails_to_do
        email_to_do = (int(latest_email_id) - emails_to_do) + 1
        print "going to do number %d" % email_to_do
        
        #start working on that email
        result, data = mail. fetch(latest_email_id, "(BODY[HEADER.FIELDS (FROM)])")  # fetch email body for the given id

        senderLong = data[0][1]
        #getting the subject line of the email, includes extra characters

        sender = senderLong.split('<')[1]       # keep everything after the '<'
        sender = senderLong.split('>')[0]  # keep everything before the '>'
        
        print "need to email %r about email # %d" % (sender, email_to_do)
        print "writing %d to last_email_checked" % email_to_do
        # update_list(email_to_do)
        write_to = open('/python/cubeputer/last_email_checked.txt', 'w')
        write_to.write(str(email_to_do))
        write_to.close()
        last = email_to_do  # update variable last to match what is in the txt file

        email_msg = send.generate_email(fromEmail, [sender])
        send.send_email(email_msg, fromEmail,password,[sender])


    
    
        
    
    elif int(latest_email_id) == last:
        print "No new mail"

    prev_latest_email_id = latest_email_id
    cycles += 1

    sleep(5)

except:
    sleep(5)
    errors += 1
