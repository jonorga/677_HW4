###
### CS667 Data Science with Python, Homework 4, Jon Organ
###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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


def aggData(a1, a2, a3, a4, a5, a6, a7, a8, a9, std_list):
	data = [["Age", "Duration", "Efficiency", "REM %", "Deep Sleep %", 
		"Light Sleep %", "Awakenings", "Smoking", "Exercise"]]
	if std_list:
		smoking = ["N/A"] * 5
	else:
		smoking = []

		if 'children' in a8:
			c_in_list = True
		else:
			c_in_list = False
		if 'teenagers' in a8:
			t_in_list = True
		else:
			t_in_list = False
		if 'young adults' in a8:
			y_in_list = True
		else:
			y_in_list = False
		if 'adults' in a8:
			a_in_list = True
		else:
			a_in_list = False
		if 'older adults' in a8:
			o_in_list = True
		else:
			o_in_list = False
		

		if c_in_list:
			if len(a8['children'].index) == 1:
				temp = a8['children']
				if 'Yes' in temp:
					smoking.append("Yes")
				elif 'No' in temp:
					smoking.append("No")
				else:
					smoking.append("N/A")
			elif a8["children", "Yes"] > a8["children", "No"]:
				smoking.append("Yes")
			else:
				smoking.append("No")
		else:
			smoking.append("N/A")

		if t_in_list:
			if len(a8['teenagers'].index) == 1:
				temp = a8['teenagers']
				if 'Yes' in temp:
					smoking.append("Yes")
				elif 'No' in temp:
					smoking.append("No")
				else:
					smoking.append("N/A")
			elif a8["teenagers", "Yes"] > a8["teenagers", "No"]:
				smoking.append("Yes")
			else:
				smoking.append("No")
		else:
			smoking.append("N/A")

		if y_in_list:
			if len(a8['young adults'].index) == 1:
				temp = a8['young adults']
				if 'Yes' in temp:
					smoking.append("Yes")
				elif 'No' in temp:
					smoking.append("No")
				else:
					smoking.append("N/A")
			elif a8["young adults", "Yes"] > a8["young adults", "No"]:
				smoking.append("Yes")
			else:
				smoking.append("No")
		else:
			smoking.append("N/A")

		if a_in_list:
			if len(a8['adults'].index) == 1:
				temp = a8['adults']
				if 'Yes' in temp:
					smoking.append("Yes")
				elif 'No' in temp:
					smoking.append("No")
				else:
					smoking.append("N/A")
			elif a8["adults", "Yes"] > a8["adults", "No"]:
				smoking.append("Yes")
			else:
				smoking.append("No")
		else:
			smoking.append("N/A")

		if o_in_list:
			if len(a8['older adults'].index) == 1:
				temp = a8['older adults']
				if 'Yes' in temp:
					smoking.append("Yes")
				elif 'No' in temp:
					smoking.append("No")
				else:
					smoking.append("N/A")
			elif a8["older adults", "Yes"] > a8["older adults", "No"]:
				smoking.append("Yes")
			else:
				smoking.append("No")
		else:
			smoking.append("N/A")

	inputs = [a1, a2, a3, a4, a5, a6, a7, a9]

	for val in inputs:
		if 'children' not in val:
			val["children"] = "N/A"
		if 'teenagers' not in val:
			val["teenagers"] = "N/A"
		if 'young adults' not in val:
			val["young adults"] = "N/A"
		if 'adults' not in val:
			val["adults"] = "N/A"
		if 'older adults' not in val:
			val["older adults"] = "N/A"


	data.append([a1["children"], a2["children"], a3["children"], a4["children"], a5["children"], a6["children"],
				a7["children"], smoking[0], a9["children"]])
	data.append([a1["teenagers"], a2["teenagers"], a3["teenagers"], a4["teenagers"], a5["teenagers"], a6["teenagers"],
				a7["teenagers"], smoking[1], a9["teenagers"]])
	data.append([a1["young adults"], a2["young adults"], a3["young adults"], a4["young adults"], a5["young adults"], 
				a6["young adults"], a7["young adults"], smoking[2], a9["young adults"]])
	data.append([a1["adults"], a2["adults"], a3["adults"], a4["adults"], a5["adults"], a6["adults"],
				a7["adults"], smoking[3], a9["adults"]])
	data.append([a1["older adults"], a2["older adults"], a3["older adults"], a4["older adults"], a5["older adults"], 
				a6["older adults"], a7["older adults"], smoking[4], a9["older adults"]])

	return data


def generateTable(data, name):
	data = zip(*data)
	df = pd.DataFrame(data, columns=[name, 'Children', 'Teenagers', 'Young Adults', 'Adults', 'Older Adults'])
	fig, ax = plt.subplots()
	fig.patch.set_visible(False)
	ax.axis('off')
	ax.axis('tight')
	ax.table(cellText=df.values, colLabels=df.columns, loc='center')

	print("Saving", name, "Table...")
	fig.savefig(name + "_Table.png", dpi=1200)





b_avg_data = aggData(b_avg_age, b_avg_sleepDuration, b_avg_sleepEfficiency, b_avg_remSleepPercentage, b_avg_deepSleepPercentage,
	b_avg_lightSleepPercentage, b_avg_awakenings, b_avg_smokingStatus, b_avg_exerciseFrequency, False)
b_std_data = aggData(b_std_age, b_std_sleepDuration, b_std_sleepEfficiency, b_std_remSleepPercentage, b_std_deepSleepPercentage,
	b_std_lightSleepPercentage, b_std_awakenings, b_avg_smokingStatus, b_std_exerciseFrequency, True)

m_avg_data = aggData(m_avg_age, m_avg_sleepDuration, m_avg_sleepEfficiency, m_avg_remSleepPercentage, m_avg_deepSleepPercentage,
	m_avg_lightSleepPercentage, m_avg_awakenings, m_avg_smokingStatus, m_avg_exerciseFrequency, False)
m_std_data = aggData(m_std_age, m_std_sleepDuration, m_std_sleepEfficiency, m_std_remSleepPercentage, m_std_deepSleepPercentage,
	m_std_lightSleepPercentage, m_std_awakenings, m_avg_smokingStatus, m_std_exerciseFrequency, True)

f_avg_data = aggData(f_avg_age, f_avg_sleepDuration, f_avg_sleepEfficiency, f_avg_remSleepPercentage, f_avg_deepSleepPercentage,
	f_avg_lightSleepPercentage, f_avg_awakenings, f_avg_smokingStatus, f_avg_exerciseFrequency, False)
f_std_data = aggData(f_std_age, f_std_sleepDuration, f_std_sleepEfficiency, f_std_remSleepPercentage, f_std_deepSleepPercentage,
	f_std_lightSleepPercentage, f_std_awakenings, f_avg_smokingStatus, f_std_exerciseFrequency, True)


generateTable(b_avg_data, "Both_Averages")
generateTable(b_std_data, "Both_Deviation")

generateTable(m_avg_data, "Male_Averages")
generateTable(m_std_data, "Male_Deviation")

generateTable(f_avg_data, "Female_Averages")
generateTable(f_std_data, "Female_Deviation")


# Question 6 =================================================================
print("\nQuestion 6:")
print("Female children sleep the most with an average sleep duration of 8.375")
print("Male adults sleep the least with an average sleep duration of 7.398")
print("Female children wake up the most with an average of 2.5 awakenings per night")
print("Female young adults wake up the least with an average of 1.441 awakenings per night")


# Question 7 =================================================================
print("\nQuestion 7:")
print("Male adults have the highest sleep effeciency at 80.6%")
print("Female children have the lowest sleep effeciency at 54.25%")


# Question 8 =================================================================
print("\nQuestion 8:")
print("In general, the more exercise a person gets, the less they sleep")


# Question 9 =================================================================
print("\nQuestion 9:")
print("In general, the averages table shows that smokers sleep more than non-smokers")


# Question 10 =================================================================
print("\nQuestion 10:")
print("The first thing I noticed about the table is the lower number of participants under the age"
	+ "\nof teenager results in the children and teenager groups having much more volatile answers."
	+ "\nThis is further seen in the male tables given that there are no children or teenagers in"
	+ "\nthe male group at all. One other prevalent are is that deep sleep percentages are much"
	+ "\nlower for children and teenagers, where as light sleep is significantly higher for these"
	+ "\ngroups. The largest areas of deviation in general are in the REM sleep for the all adults."
	+ "\nAdults seem to have the largest deviation but this could be due to the larger sample size.")





