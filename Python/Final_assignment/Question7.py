"""
Write a code in python using list 
To Find mean, median, mode for the given set of numbers in a list.
to print the numbers of a list after removing even numbers from i

"""
import collections

num_list = [21, 11, 19, 3,11,5]
# FInd sum of the numbers
num_sum = sum(num_list)
#divide the sum with length of the list
mean = num_sum / len(num_list)
print(num_list)
print("Mean of the above list of numbers is: " + str(round(mean,2)))


#MEDIAN
# Sort the list
num_list.sort()
# Finding the position of the median
if len(num_list) % 2 == 0:
   first_median = num_list[len(num_list) // 2]
   second_median = num_list[len(num_list) // 2 - 1]
   median = (first_median + second_median) / 2
else:
   median = num_list[len(num_list) // 2]
print(num_list)
print("Median of above list is: " + str(median))



#MODE
# calculate the frequency of each item
data = collections.Counter(num_list)
data_list = dict(data)

# Print the items with frequency
print(data_list)

# Find the highest frequency
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(num_list):
   print("No mode in the list")
else:
   print("The Mode of the list is : " + ', '.join(map(str, mode_val)))