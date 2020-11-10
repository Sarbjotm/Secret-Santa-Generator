import random 
import config
import smtplib

namesAndEmails = { #NAME: #EMAIL, 

    }

listOfNames = [] #ENTER NAMES HERE
listOfNamesLeft = [] #ENTER NAMES HERE



server =  smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        

for i in listOfNames:
    while True:
        giftee = random.choice(listOfNamesLeft)
        if(giftee == i):
            continue
        else:
            break

    subject = "Testing Python Script"
    body = "Hello " + i + "\n\nWe would like to thank you for partcipating in our first Secret Santa Event. \n\n" + "Before we tell you who your giftee will be, we'd like to remind you of a few rules \n" + " \
        1. No troll gifts are allowed, if you do bring a troll gift, your secret santa gift will be given to your giftee. \n \
        2. Stay within the set budget of $0 to $x \nNow what you were waiting for, you will be " + giftee +"'s Secret Santa! \n\nWe'll be giving out gifts virtually on Month Date Year @ Time"
    message = 'Subject: {} \n\n{}'.format(subject,body)
    server.sendmail(config.EMAIL_ADDRESS, namesAndEmails.get(i), message)
    print("Sent email!")
    listOfNamesLeft.remove(giftee)
    

server.quit()
    
    

