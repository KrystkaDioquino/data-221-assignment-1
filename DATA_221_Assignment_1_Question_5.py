import math

#Define a function to compute the percentage of the larger circle that can be covered by the smaller one
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):

    #This checks if both radii is greater than 0.
    if radiusOfCircle1 > 0 and radiusOfCircle2 > 0:

        #Calculates the area of each circle using the formula πr^2
        areaOfCircle1 = math.pi * (radiusOfCircle1 ** 2)
        areaOfCircle2 = math.pi * (radiusOfCircle2 ** 2)

        #Determine which of the two areas is larger.
        largerCircle, smallerCircle = max(areaOfCircle1, areaOfCircle2), min(areaOfCircle1, areaOfCircle2)

        #Compute the percenatge of the larger circle that can be covered by the smaller circle.
        percentOfLargerCirleCoveredBySmallerCircle = (smallerCircle/largerCircle) *100

        #Returns the percentage
        return percentOfLargerCirleCoveredBySmallerCircle

    #If one of the radius is 0, the cirle doesn't exist. This will result to returning an invalid message.
    else:
        return ("Error!\nThe value of both radii must be a positive number. Please run the program again.")

#Asks the user to enter the first radius value.
radiusOfCircle1= int(input("Enter the value of the first radius of the circle: "))

#Asks the user to enter the second radius value.
radiusOfCircle2 = int(input("Enter the value of the second radius of the circle: "))

#Calls the function and stores the result
percentageCoveredResult = circleAreaCoverage(radiusOfCircle1, radiusOfCircle2)

#Displays the final result.
print(f"The percentage of the larger circle that can be covered by the smaller circle is {percentageCoveredResult:.2f}%")
