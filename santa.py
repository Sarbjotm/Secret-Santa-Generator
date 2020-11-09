import random 

listOfNames = [] #ENTER NAMES HERE
listofNamesChoosen = []

for i in range(len(listOfNames)):
    while True:
        r = random.randint(0,len(listOfNames)-1)
        if(listOfNames[r] == listOfNames[i] or listOfNames[r] in listofNamesChoosen):
            continue
        else:
            break
    print(f"{listOfNames[i]} will give a gift to {listOfNames[r]}")
    listofNamesChoosen.append(listOfNames[r])
    
    

