#This asks the user to input an integer that will be the basis of the greater than or equal to comparison
thresholdLimitValue = int(input("Enter your threshold: "))

#Initialize the product value of the consecutive integers to 1
currentProductOfTheConsecutiveIntegers = 1

#Initialize the integer that will be multiplied each iteration
currentNumberToMultiply = 0


#A while loop to keep executing until the current product of the integers is greater than or equal to the threshold
while currentProductOfTheConsecutiveIntegers <= thresholdLimitValue:

    #Adds 1 to the integer to multiply the current product with.
    currentNumberToMultiply += 1

    #Multiply the current product by the new integer
    currentProductOfTheConsecutiveIntegers *= currentNumberToMultiply

#This displays the final product and the integer that caused it to exceed or be equal to the threshold.
print(f"The final product is {currentProductOfTheConsecutiveIntegers} and the integer than caused it"
      f" to exceed the threshold of {thresholdLimitValue} is {currentNumberToMultiply}.")