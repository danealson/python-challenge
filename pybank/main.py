#Dependencies
import os
import csv

#Path of CSV
budget_csv = os.path.join("resources", "budget.csv")

#Set to CSV
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #header
    csv_header = next(csv_reader)

    #Define variables 
    months = []
    profits = []

    for row in csv_reader:
        months.append(row[0])
        profits.append(row[1])

    total_months = len(months)

    # print(f'Total Months: {total_months}')

    #Add profits 
    revenue = 0
    i = 1
    for i in range(total_months):
        revenue = revenue + int(profits[i])
    # print(f'Total Revenue: ${revenue}')

    #Figure out the change
    change = []
    j = 0
    k = 0

    for j in range (1, total_months):
        if j == 0:
            change.append(0)
        else:
            change.append(int(profits[j])-int(profits[k]))
            k += 1
    #print(change)

    #sum of the monthy changes with average
    average_month = ((sum(change))/(len(change)))
    # print(f"Average Change: ${round((average_month),2)}")

    #Great Increase in Profits
    max_change = max(change)
    # print(f"Greatest Increase in Revenuse: ${max_change}")
    #Greatest Decrease in Profits
    min_change = min(change)
    # print(f"Greatest Decrease in Revenues: ${min_change}")


print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${revenue}")
print(f"Average Change: ${average_month}")
print(f"Greatest Increase in Profits: ${max_change}")
print(f"Greatest Decrease in Profits: ${min_change}")

output_file = 'analysis/results.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${revenue}"])
    csvwriter.writerow([f"Average Change: ${average_month}"])
    csvwriter.writerow([f"Greatest Increase in Profits: ${max_change}"])
    csvwriter.writerow([f"Greatest Decrease in Profits: ${min_change}"])