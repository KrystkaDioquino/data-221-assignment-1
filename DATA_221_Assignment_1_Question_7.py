def secondsToStandardTime(secondsToConvert):

    #Validates the input is numeric.
    if not isinstance(secondsToConvert, (int, float)):
        return "Invalid! Input should be a numeric value."

    #Validates the input is a non-negative number.
    elif secondsToConvert < 0:
        return "Invalid! Input is less than 0 and cannot be converted."

    else:
        #This determine if time is in AM or PM. 43200 seconds is used as it is equivalent to 12 hours
        if secondsToConvert >= 43200:
            timeOfDay = "PM"
        else:
            timeOfDay = "AM"

        #Initialize variables that will calculate the hours, minutes, and seconds.

        #Calculate total hours. 3600 seconds is equivalentto 1 hour.
        hoursInStandardTime = secondsToConvert // 3600

        #Calculate the remaining seconds after hours being removed.
        remainingSeconds = secondsToConvert % 3600

        #Calculate total minutes from the remaining seconds. 60 seconds is equivalent to 1 minute.
        minutesInStandardTime = remainingSeconds // 60

        #Calculates the final remaining seconds after getting the minutes.
        secondsInStandardTime = remainingSeconds % 60

        #This equates having 0 hours to default value of 12 since the standard time starts at 12 AM.
        if hoursInStandardTime == 0:
            hoursInStandardTime = 12

    #This returns a neatly formated string accordingly to how we see time.
    return (f"{hoursInStandardTime} {minutesInStandardTime:02d} {secondsInStandardTime:02d} {timeOfDay}")

#These are the test cases. Arguments can be changed.
print(secondsToStandardTime(10000))
print(secondsToStandardTime(120))
print(secondsToStandardTime(40000))
print(secondsToStandardTime(-44))
print(secondsToStandardTime("Time"))
