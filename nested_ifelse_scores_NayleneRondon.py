#Purpose: Depicts if-else statements to determine grade. 
#Date: 2/1/17
#Programmer: Naylene Rondon
#FileName: nested_ifelse_scores_NayleneRondon.py

#Start
print("What is your letter grade base off percentage? ")

#Variable
grade = float(input("Type in your score: "))

#Process
if grade >= 89.5:
    print("You have an A.")
elif grade >= 79.5:
     print("You have a B.")
elif grade >= 69.5:
    print("You have a C.")
elif grade >= 59.5:
    print("You have a D.")
else:
    print("You have an F.")

#End
