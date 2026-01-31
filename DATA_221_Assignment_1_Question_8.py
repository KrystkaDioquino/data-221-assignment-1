import pandas as pd

#Initialize a dictionary named data with a list of numbers as values
data = {
    "A": [1,2,2,1],
    "B": [3.1,4.2,1.5,6.3],
    "C": [800,150,400,210]
}

#Make a data frame with the data dictionary using pandas DataFrame object
data_frame = pd.DataFrame(data)

#Creates a new column named D from adding the values from column A B and C
data_frame["D"] = data_frame["A"] + data_frame["B"] + data_frame[("C")]

#Displays the complete data frame
print(data_frame)