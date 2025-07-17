import numpy as np

week_spendings = np.array([50, 120, 30, 40, 200, 90, 300])
index = np.argmax(week_spendings)  # returns index of the max value
big_spending = week_spendings[index]  # actual max value

# map index 0–6 to days
days = {0:'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'}
for i in range(len(week_spendings)):
	if week_spendings[i] > big_spending:
		big_spending = week_spendings[i]
		index = i
print(big_spending, days[index])
print(i)
