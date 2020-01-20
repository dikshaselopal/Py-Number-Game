
print("---Number Guess Game Between 0-20---")
import random
start=0
end=20
computerNumber=random.randint(0,21)
while(True):
    userNumber=int(input("Enter your Number: "))
    if(computerNumber == userNumber):
        print("Your Guess is correct!!!")
        break
    elif(computerNumber > userNumber):
        end=computerNumber
        midnumber=(start+end)/2
        print(midnumber)
        if(midnumber > userNumber):
            print("Your Number is Low")
        else:
            print("Too Low")   
    elif(computerNumber < userNumber):
        start=computerNumber
        midnumber=(start+end)/2
        print(midnumber)
        if(midnumber < userNumber):
            print("Your Number is High")
        else:
            print("Too HIGH")
            
    else:
        print("Not a valid Input")
