###
### CS667 Data Science with Python, Homework 4, Jon Organ
###

import pandas as pd
import matplotlib.pyplot as plt
import math
Nonetype = type(None)

file_cmg = pd.read_csv("cmg_with_color.csv")
file_spy = pd.read_csv("spy_with_color.csv")



def GenerateDF(working_file):
	output = pd.DataFrame(columns=['Week', 'Color', 'Avg Return', 'Volatility'])
	file_len = len(working_file.index)
	i = 0
	count = 0
	while i < file_len:
		if working_file["Color"].get(i) == "Undefined":
			i = file_len
		elif working_file["Weekday"].get(i) == "Friday":
			week_len = 1
			while working_file["Weekday"].get(i + week_len) != "Friday":
				week_len += 1

			j = 0
			avg_return = 0
			while j < week_len:
				avg_return += working_file["Return"].get(i + j)
				j += 1
			avg_return /= week_len

			volatility = 0
			dist_from_avg = 0
			j = 0
			while j < week_len:
				dist_from_avg += abs(working_file["Return"].get(i + j) - avg_return) ** 2
				j += 1
			volatility = math.sqrt(dist_from_avg / week_len)

			if working_file["Color"].get(i + week_len) != "Undefined":
				output.at[count, "Week"] = count + 1
				output.at[count, "Color"] = working_file["Color"].get(i + week_len)
				output.at[count, "Avg Return"] = avg_return
				output.at[count, "Volatility"] = volatility
			count += 1
			i = i + week_len - 1
		i += 1
	return output

output_cmg = GenerateDF(file_cmg)
output_spy = GenerateDF(file_spy)



def GeneratePlot(frame, name):
	scatter_plot = plt.figure()
	axes1 = scatter_plot.add_subplot(1, 1, 1)
	axes1.scatter(frame["Avg Return"], frame["Volatility"], color=frame["Color"], s=50)
	axes1.set_title("Average Return vs Volatility for " + name)
	axes1.set_xlabel("Average Return")
	axes1.set_ylabel("Volatility")
	scatter_plot.savefig(name + "_Avg_Return_VS_Volatility.png")

GeneratePlot(output_cmg, "CMG")
GeneratePlot(output_spy, "SPY")

