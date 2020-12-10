import os
import csv 

#point to data
budget_data = os.path.join("Resources", "budget_data.csv")
#point location for output
financial_analysis = os.path.join("Analysis", "Financial_Analysis_output.txt")

#open data and separate by dilimeter
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    #skip header (first) row
    csv_header = next(csv_reader) 
    
    #create lists for appenderd looped values 
    pl_change = []
    month_change = []
    total_change = []
    #define and start values
    total_months = 0
    total_pl = 0
    average_change = 0
    i = 0
    max_profit = 0
    min_profit = 0
   
    #First loop runs through totals 
    for row in csv_reader:
        total_months = total_months + 1        
        total_pl += int(row[1])        
        
        total_change = [] 
        pl_change.append(int(row[1]))
        month_change.append(row[0]) 
        
        #second loop to calulculate average change and look at previous change
        for i in range(1 , len(pl_change)): 
                #append values from previous to curent looped value
             total_change.append(pl_change[i]-(pl_change[i-1])) 

#find the average change using what we found in total change 
average_change = round(sum(total_change)/ len(total_change),2)

#find min and max values
max_profit = max(total_change) 
min_profit = min(total_change)
#index the max and min change to find max and min month
max_month = total_change.index(max_profit) + 1
min_month = total_change.index(min_profit) + 1 

#define reults of what we found to print in text file
analysis = ("Financial Analysis\n" 
"-------------------------------------------------\n"
f"Total Months: {total_months}\n"
f"Change Over Period: ${total_pl}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profit: {month_change[max_month]} : ${max_profit}\n"
f"Greatest Decrease in Profit: {month_change[min_month]} : ${min_profit}")

#show the results in terminal as well
print(analysis)

#make a text file with the financial analysis using above
with open(financial_analysis, "w") as txt_file: 
    txt_file.write(analysis)