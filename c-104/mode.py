# importing module 
import csv
from typing import Counter

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

# converting that list into dictionary whose keys are the heights and values are their occurance
data = Counter(new_data)

# making a dictionary with keys as the category of numbers and the values as the occurance which is initally zero 
mode_for_range = {"60-65": 0, "65-70": 0, "70-75": 0}

# getting into data by data.items() which has two index first one is height and second is occurance 
# then increasing the occurance in the category in which the height lie
for height, occurance in data.items():
    if 60 < float(height) < 65:
        mode_for_range["60-65"] += occurance

    elif 65 < float(height) < 70:
        mode_for_range["65-70"] += occurance

    elif 70 < float(height) < 75:
        mode_for_range["70-75"] += occurance

mode_range, mode_occurance = 0, 0

# getting into data by mode_for_range.items() which has two index first one is range and second is occurance 
for range, occurance in mode_for_range.items():
    # checking if occurance of any category is greater than the value present in mode_occurance
    if occurance > mode_occurance:
        # if yes then the value before and after '-' placed at index no. 0 and 1 
        # and mode_occurance = occurance
        mode_range, mode_occurance = [int(range.split('-')[0]), int(range.split('-')[1])], occurance

# finding mode by adding the value index no. 0 and 1 and then dividing it by 2
mode = float((mode_range[0] + mode_range[1]) / 2)

# printing the mode 
print(mode)
