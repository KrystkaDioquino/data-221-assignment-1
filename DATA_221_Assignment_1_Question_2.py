#Function that takes a list of keys and returns a dictionary with the key's length and parity
def getStringLengthAndParity(listOfKeys):\

    #Creates am empty dictionary to store string information later
    dictionaryWithStringInformation = {}

    #This loops through each element of the list
    for key in listOfKeys:

        #Gets the length of the key of the dictionary
        lengthOfStringKey = len(key)

        #Check if the lenght of the key is odd or even
        if lengthOfStringKey % 2 == 0:
            parityOfStringKey = "even"
        else:
            parityOfStringKey = "odd"

        #Stores the string information of the key in the dictionary
        dictionaryWithStringInformation[key] = {
            "length" : lengthOfStringKey,
            "parity" : parityOfStringKey
        }

    #Returns the dictionary with complete string information
    return dictionaryWithStringInformation

#Creates a list of string keys
listOfKeys =["data", "science"]

#Calls the function and store the returned dictionary to the variable
dictionaryWithStringInformation = getStringLengthAndParity(listOfKeys)

#This loops through the returned dictionary to display the key and its values in a readable format
for key, info in dictionaryWithStringInformation.items():
    print(f"{key}: {info}")