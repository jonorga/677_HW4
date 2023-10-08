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

print("Values imputed...\n")
# Question 5 =================================================================
print("Question 5:")
conditions = [
	(file['Age'] <= 12),
	(file['Age'] > 12) & (file['Age'] <= 17),
	(file['Age'] > 17) & (file['Age'] <= 30),
	(file['Age'] > 30) & (file['Age'] <= 60),
	(file['Age'] > 60)
	]

values = ['children', 'teenagers', 'young adults', 'adults', 'older adults']

file['Group'] = np.select(conditions, values)
print("Groups assigned based on age...")
file_m = file[file["Gender"] == "Male"]
file_f = file[file["Gender"] == "Female"]

# Need 6 total tables
#	Standard deviation and mean for males, females, and both
b_avg_age = file.groupby('Group')['Age'].mean()
b_avg_sleepDuration = file.groupby('Group')['Sleep duration'].mean()
b_avg_sleepEfficiency = file.groupby('Group')['Sleep efficiency'].mean()
b_avg_remSleepPercentage = file.groupby('Group')['REM sleep percentage'].mean()
b_avg_deepSleepPercentage = file.groupby('Group')['Deep sleep percentage'].mean()
b_avg_lightSleepPercentage = file.groupby('Group')['Light sleep percentage'].mean()
b_avg_awakenings = file.groupby('Group')['Awakenings'].mean()
b_avg_smokingStatus = file.groupby('Group')['Smoking status'].value_counts()
b_avg_exerciseFrequency = file.groupby('Group')['Exercise frequency'].mean()

m_avg_age = file_m.groupby('Group')['Age'].mean()
m_avg_sleepDuration = file_m.groupby('Group')['Sleep duration'].mean()
m_avg_sleepEfficiency = file_m.groupby('Group')['Sleep efficiency'].mean()
m_avg_remSleepPercentage = file_m.groupby('Group')['REM sleep percentage'].mean()
m_avg_deepSleepPercentage = file_m.groupby('Group')['Deep sleep percentage'].mean()
m_avg_lightSleepPercentage = file_m.groupby('Group')['Light sleep percentage'].mean()
m_avg_awakenings = file_m.groupby('Group')['Awakenings'].mean()
m_avg_smokingStatus = file_m.groupby('Group')['Smoking status'].value_counts()
m_avg_exerciseFrequency = file_m.groupby('Group')['Exercise frequency'].mean()

f_avg_age = file_f.groupby('Group')['Age'].mean()
f_avg_sleepDuration = file_f.groupby('Group')['Sleep duration'].mean()
f_avg_sleepEfficiency = file_f.groupby('Group')['Sleep efficiency'].mean()
f_avg_remSleepPercentage = file_f.groupby('Group')['REM sleep percentage'].mean()
f_avg_deepSleepPercentage = file_f.groupby('Group')['Deep sleep percentage'].mean()
f_avg_lightSleepPercentage = file_f.groupby('Group')['Light sleep percentage'].mean()
f_avg_awakenings = file_f.groupby('Group')['Awakenings'].mean()
f_avg_smokingStatus = file_f.groupby('Group')['Smoking status'].value_counts()
f_avg_exerciseFrequency = file_f.groupby('Group')['Exercise frequency'].mean()


b_std_age = file.groupby('Group')['Age'].std()
b_std_sleepDuration = file.groupby('Group')['Sleep duration'].std()
b_std_sleepEfficiency = file.groupby('Group')['Sleep efficiency'].std()
b_std_remSleepPercentage = file.groupby('Group')['REM sleep percentage'].std()
b_std_deepSleepPercentage = file.groupby('Group')['Deep sleep percentage'].std()
b_std_lightSleepPercentage = file.groupby('Group')['Light sleep percentage'].std()
b_std_awakenings = file.groupby('Group')['Awakenings'].std()
b_std_exerciseFrequency = file.groupby('Group')['Exercise frequency'].std()

m_std_age = file_m.groupby('Group')['Age'].std()
m_std_sleepDuration = file_m.groupby('Group')['Sleep duration'].std()
m_std_sleepEfficiency = file_m.groupby('Group')['Sleep efficiency'].std()
m_std_remSleepPercentage = file_m.groupby('Group')['REM sleep percentage'].std()
m_std_deepSleepPercentage = file_m.groupby('Group')['Deep sleep percentage'].std()
m_std_lightSleepPercentage = file_m.groupby('Group')['Light sleep percentage'].std()
m_std_awakenings = file_m.groupby('Group')['Awakenings'].std()
m_std_exerciseFrequency = file_m.groupby('Group')['Exercise frequency'].std()

f_std_age = file_f.groupby('Group')['Age'].std()
f_std_sleepDuration = file_f.groupby('Group')['Sleep duration'].std()
f_std_sleepEfficiency = file_f.groupby('Group')['Sleep efficiency'].std()
f_std_remSleepPercentage = file_f.groupby('Group')['REM sleep percentage'].std()
f_std_deepSleepPercentage = file_f.groupby('Group')['Deep sleep percentage'].std()
f_std_lightSleepPercentage = file_f.groupby('Group')['Light sleep percentage'].std()
f_std_awakenings = file_f.groupby('Group')['Awakenings'].std()
f_std_exerciseFrequency = file_f.groupby('Group')['Exercise frequency'].std()


def aggData(a1, a2, a3, a4, a5, a6, a7, a8, a9):
	print(a1["children"])


b_avg_data = ["Age", "Duration", "Efficiency", "REM %", "Deep Sleep %",
 "Light Sleep %", "Awakenings", "Smoking", "Exercise"]


aggData(b_avg_age, b_avg_sleepDuration, b_avg_sleepEfficiency, b_avg_remSleepPercentage, b_avg_deepSleepPercentage,
	b_avg_lightSleepPercentage, b_avg_awakenings, b_avg_smokingStatus, b_avg_exerciseFrequency)

