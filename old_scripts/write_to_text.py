#reads to/ pulls from a file called dict.txt

import os

last = eval(open("last_email_checked.txt").read())
print last

if last == 23:
    print "yep"


write_to = open('last_email_checked.txt', 'w')
a = str(23)
write_to.write(a)


write_to.close()



