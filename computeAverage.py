howManyEntered = 0
total = 0
average = 0
#this line inputs how many test scores user wants to enter
howMany = int (input ("How many test scores would you like to average? "))
while howManyEntered <= howMany:
    #this line allows user to enter a score and then stores it in testScore
    testScore = int(input ("Enter test score: "))
    howManyEntered = howManyEntered 
    total = total + testScore
    average = total/howMany
print ("The average is: " + str(average))
    

