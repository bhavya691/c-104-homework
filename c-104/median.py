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

# positioning the numbers in list in ascending/increasing order 
new_data.sort()

# checking if the length of new_data list is even or odd
if n % 2 == 0:
    # if even then find median using formula (n-1+n)/2
    m1 = float(new_data[n//2])
    m2 = m1-1
    median = (m1+m2)/2
else:
    # if odd then find median using formula n/2
    median = new_data[n//2]
# printing median 
print(median)