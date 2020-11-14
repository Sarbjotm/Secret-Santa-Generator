import csv
import random 
import config
import smtplib


class partcipatants:
    def __init__(self, name, email, discordName, mailingAddress, deliver, preferences, nogift, allergies, whatAllergies):
        self.name = name
        self. email = email
        self.discordName = discordName
        self.mailingAddress = mailingAddress
        self.deliver = deliver
        self.preferences = preferences
        self.nogift = nogift
        self.allergies = allergies
        self.whatAllergies = whatAllergies

users = []
usersLeft = []


fileCSV = open('namesandemails.csv','r')
reader = csv.reader(fileCSV)
for row in reader:
    try:
        users.append( partcipatants(row[1],row[3], row[2],row[4], row[5], row[6], row[7],row[8],row[9]))
        usersLeft.append( partcipatants(row[1],row[3], row[2],row[4], row[5], row[6], row[7],row[8],row[9]))

    except:
        pass 


server =  smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.EMAIL_ADDRESS,config.PASSWORD)
        

for i in users:
    while True:
        giftee = random.choice(usersLeft)
        if(giftee.email == i.email):
            continue
        else:
            break
    
    
    subject = "Testing Python Script"
    body = "Hello " + i.name + "\n\nWe would like to thank you for partcipating in our first Secret Santa Event. \n\n" + "Before we tell you who your giftee will be, we'd like to remind you of a few rules \n" + " \
        1. No troll gifts are allowed, if you do bring a troll gift, your secret santa gift will be given to your giftee. \n \
        2. Stay within the set budget of $0 to $15 \nNow what you were waiting for, you will be " + giftee.name +"'s Secret Santa! \n\n Here are a few details about " + giftee.name + "\n" + " \
        -Their Discord username is: " + giftee.discordName + "\n" + "\
        -They would like " + giftee.preferences + " and dislike " + giftee.nogift +"\n\nWe will be giving out gifts virtually on December 22nd 2020. Please make sure you have your gift delivered before then."
    message = 'Subject: {} \n\n{}'.format(subject,body)
    server.sendmail(config.EMAIL_ADDRESS, i.email, message)
    print("Sent email!")
    del usersLeft[usersLeft.index(giftee)]    

server.quit()
    
    

