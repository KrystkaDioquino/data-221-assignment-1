from random import random

#Creates a list of 20 random values between 0 and 1 using random()
listOfRandomValues = [random() for i in range(20)]

#Generates a random value that will be used to find greater than or equal matches.
randomValueToFindAMatch = random()

#Sorts the list of random values in ascending order.
sortedListOfRandomValues = sorted(listOfRandomValues)

#Creates an empty list to store matched values later.
listOfValuesGreaterThanOrEqualToTheRandomValue = []

#Loops through the sorted list to find the first matching number.
for i in range(len(sortedListOfRandomValues)):
    if randomValueToFindAMatch <= sortedListOfRandomValues[i]:
        firstMatchedIndex = sortedListOfRandomValues[i]
        numberOfMatchedIndex = 1

        break #Stops after finding the first match

#Loops through the sorted list and find all greater than or equal random values and append it to the empty list
for j in range(len(sortedListOfRandomValues)):
    if sortedListOfRandomValues[j] >= randomValueToFindAMatch:
        listOfValuesGreaterThanOrEqualToTheRandomValue.append(sortedListOfRandomValues[j])

#Displays the sorted list
print("The sorted list: ", sortedListOfRandomValues)

#Prints ou the random value
print("The value of x: ", randomValueToFindAMatch)

#Check if there is a matching value to display correct message.
if numberOfMatchedIndex != 0:
    print("The first matching index: ", firstMatchedIndex)
else:
    print("There's no values greater than or equal to", randomValueToFindAMatch)