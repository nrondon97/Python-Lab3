#Purpose: A program that continuously ask for your
#Name, Age, and Salary
#Date: 1/31/17
#Programmer: Naylene Rondon
#FileName: while_salary_NayleneRondon.py

#Start
print("Please type your name, age, and salary. Type \"quit\" to escape.")

#Constant Variable
name = ""
#Loop
while (name != "quit"):
       name = input("What is your name: ")
       if name == "quit" :                    #Allow user to escape
           break
       age = input("What is your age: ")
       salary = input("What is your salary: ")


#End
