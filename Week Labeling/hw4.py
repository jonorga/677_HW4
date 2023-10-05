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


def y2BuynHold(file_len, working_file):
	i = 0
	first_day = True
	while i < file_len:
		temp = working_file["Date"].get(i)
		if type(temp) != Nonetype:
			if temp.split("/")[2] == "18" and first_day:
				initial_price = working_file["Adj Close"].get(i)
				your_stock = 100 / initial_price
				first_day = False
			if temp.split("/")[2] == "19":
				final_price = working_file["Adj Close"].get(i - 1) * your_stock
				i = file_len
		i += 1
	#print("For the " + file_name + " stock, using buy and hold, the start balance was $100.00, the end balance was $" 
	#	+ str(round(final_price, 2)))
	return final_price

cmg_bnh_final = y2BuynHold(file_len_cmg, file_cmg)
spy_bnh_final = y2BuynHold(file_len_spy, file_spy)

def y2LabelTrade(file_len, working_file):
	i = 0
	balance = 100
	first_day = -1
	last_day = -1
	in_cash = True
	your_stock = 0
	while i < file_len:
		temp = working_file["Date"].get(i)
		if type(temp) != Nonetype:
			if temp.split("/")[2] == "18":
				if first_day == -1:
					first_day = i
				if balance <= 0:
					last_day = i
					i = file_len
				else:
					if working_file["Color"].get(i) == "Green":
						if in_cash:
							your_stock = 100 / working_file["Adj Close"].get(i - 1)
							in_cash = False
					elif working_file["Color"].get(i) == "Red":
						if not in_cash:
							balance = your_stock * working_file["Adj Close"].get(i - 1)
							in_cash = True
		i += 1
	return balance
	#if last_day == -1:
	#	print("For the " + file_name + " stock, using the labels, the start balance was $100.00, the end balance was $" 
	#		+ str(round(balance, 2)))
	#else:
	#	print("For the " + file_name + " stock, using the labels to trade bankrupted the account after " 
	#		+ str(last_day - first_day) + " days")


cmg_label_final = y2LabelTrade(file_len_cmg, file_cmg)
spy_label_final = y2LabelTrade(file_len_spy, file_spy)

if cmg_bnh_final > cmg_label_final:
	print("For the Chipotle stock, using buy-and-hold was more effective with a final balance of $" 
		+ str(round(cmg_bnh_final, 2)) + " compared to the label trading final balance of $" 
		+ str(round(cmg_label_final, 2)))
else:
	print("For the Chipotle stock, using label trading was more effective with a final balance of $" 
		+ str(round(cmg_label_final, 2)) + " compared to the buy-and-hold final balance of $" 
		+ str(round(cmg_bnh_final, 2)))

if spy_bnh_final > spy_label_final:
	print("For the Spy stock, using buy-and-hold was more effective with a final balance of $" 
		+ str(round(spy_bnh_final, 2)) + " compared to the label trading final balance of $" 
		+ str(round(spy_label_final, 2)))
else:
	print("For the Spy stock, using label trading was more effective with a final balance of $" 
		+ str(round(spy_label_final, 2)) + " compared to the buy-and-hold final balance of $" 
		+ str(round(spy_bnh_final, 2)))


