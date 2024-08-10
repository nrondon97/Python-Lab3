#Purpose: Depicts if statements nested into a while loop determining the
#remainder of the gift certificates.
#Date: 1/30/17
#Programmer: Naylene Rondon
#FileName: giftcertificate_edited_NayleneRondon.py

#Start
print("Congrats you have $100 gift certificate.")
print("Please use this to calculate how much is available.")
name = input("What's your name? ")

#Variable
gift = float(100)
total = 0

#Input
while gift > 0:
    person = int(input("How many people are going? "))
    ticket = float(input("How much do the tickets cost? "))
    refesh = float(input("How much are the total refreshments? "))

    #Calculate
    total = float(person * ticket) + refesh
    if total > gift:  #So user doesn't spend more than they have
        break
    gift = gift - total

    #Output
    #print(name + ", the total is: " + str(total))
    #print("The remainder of your gift certificate is: " + str(gift))
    #print("Your Giftcard balance is: $"\
          #+ format(gift, ".2"), '' + 'left')

    #gift = 0 #tester variable

#End of loop
print("You have insufficent funds.")

#End
