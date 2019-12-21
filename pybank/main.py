#import os and csv so this works on all devices and can read csv files
import os
import csv
#set file path
file = os.path.join("Resources" ,"budget_data.csv")
output_path = os.path.join("budget_stats.txt")

#read csv
with open(file, newline="") as budgetcsv:
    budget = csv.reader(budgetcsv, delimiter=",")
    header = next(budget)
    #set variable value to count number of rows
    months = 0 
    total = 0
    total_change = 0 
    last_row = 0
    max_change = 0
    max_month = []
    min_change = 0
    min_month = []
    change=0
    #for loop to run analysis
    for row in budget:
        months = months +1
        total = total + int(row[1])
        if last_row != 0:
            change = int(row[1]) - last_row
            total_change = total_change + change
            if change > max_change:
                max_change = change
                max_month = row[0]
            if change < min_change:
                min_change = change
                min_month = row[0]
           
         


        
        
        
        last_row = int(row[1])
        

    avg_change = total_change/(months - 1)
    with open(output_path, 'w') as txtfile:
        txtfile.write("Financial Analysis "
        "Total Months: " + str(months)+ " " +
        "Total: " + str(total) + " " +
        "average Change: $" + '{:,.2f}'.format(avg_change) +  " " +
        "Greatest increase in profits: " + max_month + " $"  '{:,.2f}'.format(max_change) +" "+
        "Greatest decrease in profits: " + min_month + " $"  '{:,.2f}'.format(min_change))


    print("Financial Analysis")
    print("----------------------")
    print("Total Months: " + str(months))
    print("Total: " + str(total))
    print("verage  Change: $" + '{:,.2f}'.format(avg_change))
    print("Greatest increase in profits: " + max_month + " $"  '{:,.2f}'.format(max_change))
    print("Greatest decrease in profits: " + min_month + " $"  '{:,.2f}'.format(min_change))

    



