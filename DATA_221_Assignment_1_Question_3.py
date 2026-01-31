#Defines a function that takes the pair of base and exponent from a list and get its power.
def computeThePowerOfBaseAndExponentPairs(pairOfBaseAndExponent):

    #Computes the base raised to the exponent.
    computedPowerValue = pairOfBaseAndExponent[0]**pairOfBaseAndExponent[1]

    #Returns the computed power value
    return computedPowerValue

#Creates a list of a list containing the base and exponent values.
pairOfBaseAndExponentList = [[5,2], [3,-1], [4,3], [2,0]]

#Creates an empty list to later on store the computed power values
listOfComputedPowerResults = []

#Loop that allows to go through each pairs in the list
for aPairOfBaseAndExponent in pairOfBaseAndExponentList:

    #This checks if the exponent is a non-negative value.
    if aPairOfBaseAndExponent[1] < 0:
        continue #This ignores that pair of base and exponent

    #Calls the function
    computedPowerValue = computeThePowerOfBaseAndExponentPairs(aPairOfBaseAndExponent)

    #This then adds the computed power using the base and exponent to the initialized list made earlier.
    listOfComputedPowerResults.append(computedPowerValue)

#This displays the list of computed power results.
print(listOfComputedPowerResults)