import csv
import random 
import config
import smtplib


class partcipatants:
    def __init__(self, name, email, discordName, mailingAddress, deliver, preferences, nogift, allergies, whatAllergies):
        self.name = name #1
        self.email = email #3
        self.discordName = discordName #2
        self.mailingAddress = mailingAddress #4
        self.deliver = deliver #5
        self.preferences = preferences #6
        self.nogift = nogift #7
        self.allergies = allergies #8
        self.whatAllergies = whatAllergies #9

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
    
    
    subject = "[Dodo Club] - Secret Santa!"
    body = "Hello " + i.name + "\n\nWe would like to thank you for partcipating in our first Secret Santa Event. \n\n" + "Before we tell you who your giftee will be, we'd like to remind you of a few rules \n" + " \
        1. No troll gifts are allowed, if you do bring a troll gift, your secret santa gift will be given to your giftee. \n \
        2. Stay within the set budget of $0 to $15 \nNow what you were waiting for, you will be " + giftee.name +"'s Secret Santa! \n\n Here are the responses given by " + giftee.name + ": \n" + " \
        -Discord Username: " + giftee.discordName + "\n" + "\
        -Are you alright with your secret santa delivering the gift: " + giftee.deliver + "\n" + "\
        -Mailing Address: " + giftee.mailingAddress +"\n" + "\
        -Allergies: " + giftee.whatAllergies + "\n" + "\
        -Gift Preferences: " + giftee.preferences + "\n" + "\
        -Gifts they do not want: " + giftee.nogift + "\n\n" + "We will be giving out gifts/opening gifts virtually on December 22nd 2020. Please make sure you have your gift delivered before then."
    message = 'Subject: {} \n\n{}'.format(subject,body)
    server.sendmail(config.EMAIL_ADDRESS, i.email, message)
    print("Sent email!")
    del usersLeft[usersLeft.index(giftee)]    

server.quit()
    
    

