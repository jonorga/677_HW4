###
### CS667 Data Science with Python, Homework 4, Jon Organ
###

import pandas as pd
import numpy as np

# Question 1 =================================================================
file = pd.read_csv("Sleep_Efficiency.csv")


# Question 2 =================================================================
print("Question 2:")
print(file.count())


# Question 3 =================================================================
print("\nQuestion 3:")
print(file.isnull().sum())


# Question 4 =================================================================
print("\nQuestion 4:")
nan_rows = []
nan_id = []
columns = file.columns

for col in columns:
	temp = file[file[col].isnull()]
	if len(temp.index) > 0:
		nan_rows.append(temp)
		nan_id.append(col)

for _rows, _ids in zip(nan_rows, nan_id):
	a = 0
	# TODO: go through each row in _rows object
	# TODO: Find a list of people with the same gender from the whole file, excluding themselves
	# TODO: Find the five people with the closest ages, assign the average or most common label to nan
	

	# Get each row of _rows
	for index, row in _rows.iterrows():
		temp = file[(file["Gender"] == row["Gender"]) & (file[_ids] * 0 == 0)]
		temp = temp.drop(temp[temp.ID == row["ID"]].index)
		closest = temp.iloc[(temp["Age"]-row["Age"]).abs().argsort()[:5]]

		average = 0
		for index2, row2 in closest.iterrows():
			average += row2[_ids]
		average /= 5

		file.at[row["ID"] - 1, _ids] = average

print(file.isnull().sum())




