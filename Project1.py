# Yewon Lee _ CS 151 _ Project1 _ Housing

name = input ("What is your name?")
housingPt = 0

# 1st factor: Necessity of Accessibility Service 

acService = input("Are you officially approved as a student who needs accessibility services?")

if (acService == "Yes" or acService == "yes") :
    housingPt = housingPt + 30
else:
    housingPt = housingPt + 0

# 2nd factor: Grade 

grade = input("What is your grade?")

if (grade == "Senior" or grade == "senior") :
    housingPt = housingPt + 100
elif (grade == "Junior" or grade == "junior"):
    housingPt = housingPt + 90
elif (grade == "Sophomore" or grade == "sophomore"):
    housingPt = housingPt + 80
else:
    housingPt = housingPt + 70

#3rd factor: Records of rule violation

recBad = input("Do you have any record of violating the rules of your dorm or campus?")

if (recBad == "Yes" or recBad == "yes"):
    recNum = int (input ("How many records do you have?") )
    recNum = recNum * 15 
    housingPt = housingPt - recNum 
else: 
    housingPt = housingPt

# print the final result 

print ("Thank you " + name + ", your point is " + str (housingPt) + ".")



