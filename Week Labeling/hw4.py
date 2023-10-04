###
### CS667 Data Science with Python, Homework 4, Jon Organ
###

import pandas as pd
Nonetype = type(None)

file_cmg = pd.read_csv("cmg.csv")
file_spy = pd.read_csv("spy.csv")

file_cmg['Color'] = ''
file_spy['Color'] = ''

file_len_cmg = len(file_cmg.index)
file_len_spy = len(file_spy.index)

def preQ(file_len, working_file):
	i = 0
	while i < file_len:
		temp = working_file["Date"].get(i + 5)
		if type(temp) != Nonetype:
			if temp.split("/")[2] == "17" or temp.split("/")[2] == "18":
				if working_file["Weekday"].get(i) == "Friday":
					# TODO: Find next friday, weeks aren't always 5 days, some mondays skipped
					week_length = 1
					while working_file["Weekday"].get(i + week_length) != "Friday":
						week_length += 1
					if working_file["Adj Close"].get(i) < working_file["Adj Close"].get(i + week_length):
						j = 1
						while j <= week_length:
							working_file.at[i + j, "Color"] = "Green"
							j += 1
					else:
						j = 1
						while j <= week_length:
							working_file.at[i + j, "Color"] = "Red"
							j += 1
			else:
				working_file.at[i, "Color"] = "Undefined"
		i += 1
	return working_file

file_cmg = preQ(file_len_cmg, file_cmg)
file_spy = preQ(file_len_spy, file_spy)

file_cmg.to_csv("cmg_with_color.csv")
file_spy.to_csv("spy_with_color.csv")
