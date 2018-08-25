import csv

file_to_load = "C:", "Users", "bklov", "Desktop", "python-challenge", "PyBank", "budget_data.csv"
file_to_output = "analysis", "budget_data_analysis.txt"

countmonth = data["Date"].count()-1
total_profit_losses = data["Profit/Losses"].sum()
print("Financial Analysis")
print("Total Months: " + str(countmonth) )
print("Total Profit/Losses: $" + str(total_pnl) )

change = []
dictt = {}
count = 0

date = []
Date = data["Date"]
Profit/Losses = data["Profit/Losses"]
for i in range(0 , len(pnl)-1):
    profit_losses_change.append(pnl[i+1] - pnl[i])
# get number of change
for j in pnl_change:
    count = count + 1
# get total change
total_change = sum(pnl_change)
# avg change
avgprofit_losses_change = total_change / count
print("Average Profit/Losses Change: $" + str(avgpnl_change))
for a in range(0, len(pnl_change) -1):
    date.append(Date[a])

for b in range(0, len(date) -1):
    dictt[date[b]] = pnl_change[b]
    
max_incr = max(dictt.values())
min_incr = min(dictt.values())

MaxMin_date = []
for key, value in dictt.items():
    if value == max_incr:
        MaxMin_date.append(key)
    if value == min_incr:
        MaxMin_date.append(key)


print("Greatest Increase in Profit/Losses: " + str(MaxMin_date[0]) + " ($" + str(max_incr) + ")")
print("Greatest Decrease in Profit/Losses: " + str(MaxMin_date[1]) + " ($" + str(min_incr) + ")")

f = open("Output_analysis.txt" , "w")
f.write("Financial Analysis"+ "\n")
f.write("----------------------------"+ "\n")
f.write("Total Months: " + str(countmonth) + "\n")
f.write("Total Profit/Losses: $" + str(total_pnl_change)+ "\n")
f.write("Average Profit/Losses: $" + str(avg_pnl_change)+ "\n")
f.write("Greatest Increase in Profit/Losses: " + str(MaxMin_date[0]) + " ($" + str(max_incr) + ")"+ "\n")
f.write("Greatest Decrease in Profit/Losses: " + str(MaxMin_date[1]) + " ($" + str(min_incr) + ")"+"\n")
f.close()
