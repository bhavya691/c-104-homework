# importing module
import csv

# opening and reading file using csv and then converting data into list
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# removing the first index of list which is the heading so that there are only numbers
file_data.pop(0)

# making a new list
new_data = []

# going in file_data using its length
for i in range(len(file_data)):
    # getting its height as i means going through every row and 1 means index number of height
    n_num = file_data[i][1]
    # appending number in float we get in n_num
    new_data.append(float(n_num))

# finding length of new_data list
n = len(new_data)
total = 0
# finding sum of all the numbers present in the list
for x in new_data:
    total += x
# finding mean by the formula mean = sum of observation divided by no. of observation
mean = total/n

# printing mean
print(mean)
