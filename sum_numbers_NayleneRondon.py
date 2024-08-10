#Purpose: A program to calculate a sum of a series.
#Date: 2/1/17
#Programmer: Naylene Rondon
#FileName: sum_numbers_NayleneRondon.py

#Start
print("We are going to find the sum of 3, 5, 10, 15, 23, and 24")

#Variables
nums = [3, 5, 10, 15, 23, 24]   #List ##Assuming what was meant by series.
numsum = int(0)

#Process
for num in nums:   
    numsum += num   #Adding the numbers together

#Output
print("The sum of 3, 5, 10, 15, 23, and 24 is " + str(numsum))
    
#End
