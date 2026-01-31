def getPercentageDistribution(listOfNumbersToAnalyze):

    #This gets the total number of elements in the list that will be used to compute the percentage.
    totalNumberOfElementsInTheNumberList = len(listOfNumbersToAnalyze)

    #Creates a sorted version of the number list
    sortedListOfNumbersToAnalyza = sorted(listOfNumbersToAnalyze)

    #Creates an empty dictionary
    resultOfPercentageDistribution = {}

    #This loops through the numbers in the sorted list to find the unique key
    for numberInListToAnalyze in sortedListOfNumbersToAnalyza:

        #This computes the percentage of the numbers that are less than or equal to the key.
        resultOfPercentageDistribution[numberInListToAnalyze] = (
                (sum(numberFromList <= numberInListToAnalyze for
                     numberFromList in listOfNumbersToAnalyze)
                 /totalNumberOfElementsInTheNumberList) * 100)

    return resultOfPercentageDistribution

#Creates a list of number to be analyzed
listOfNumbersToAnalyze = [3,1,2,3,4,2]

#Calls the function and displays the dictionary with the percentages.
print(getPercentageDistribution(listOfNumbersToAnalyze))

