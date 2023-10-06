###
### CS667 Data Science with Python, Homework 4, Jon Organ
###

import pandas as pd

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
columns = file.columns
#for col in columns:
	#print(pd.isna(file[col]))
print(pd.isna(file["Awakenings"]))