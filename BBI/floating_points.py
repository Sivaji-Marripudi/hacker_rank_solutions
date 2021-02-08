# We wish to train a machine learning algorithm on an array of floating-point numbers in the interval [0.0,
# 1.0). The data is not evenly distributed, and we wish to filter the dataset to obtain a subset containing an
# equal number of values from each interval [0, 0.2), [0.2, 0.4), ... [0.8, 1.0), throwing away as little data as
# possible.
# Write a program which reads comma-separated floating-point numbers in a single line from stdin and prints
# the filtered data to stdout in the same format
# Note: Solve this in linear time.
# Examples:
# Example 1
# Input: 0.1,0.3,0.5,0.7,0.9
# Output: 0.1,0.3,0.5,0.7,0.9
# Question 2 – Floating PointNumbers – Print Filtered Data

# Example 2
# Input: 0.1,0.3,0.5,0.7,0.9,0.5
# Output: 0.1,0.3,0.5,0.7,0.9
# Example 3
# Input: 0.15,0.12,0.35,0.38,0.55,0.56,0.57,0.75,0.77,0.9,0.94
# Output: 0.15,0.12,0.35,0.38,0.55,0.56,0.75,0.77,0.9,0.94
# Example 4
# Input: 0.11,0.12,0.13,0.23,0.34,0.35,0.47,0.59,0.77,0.83,0.85,0.91,0.95
# On classifying the above input data from example 4, Subset in each interval will look as below:
# Interval Data
# [0 - 0.2) 0.11,0.12,0.13
# [0.2 - 0.4) 0.23,0.34,0.35
# [0.4 - 0.6) 0.47,0.59
# [0.6 - 0.8) 0.77
# [0.8 - 1.0) 0.83,0.85,0.91,0.95
# Since the interval [0.6 - 0.8) has the minimum subset of size 1. We choose 1 element from the rest of the
# intervals.
# Output: 0.11,0.23,0.47,0.77,0.83
# *if the interval [0.6 - 0.8) had more than 3 elements then we would choose 2 elements from all subset, since
# the interval with minimum subset would be [0.4 - 0.6) and of size 2.

f_numbers = list(map(float,input('enter the numbers with : ').split()))
intervals = [[0,0.2],[0.2,0.4],[0.4,0.6],[0.6,0.8],[0.8,1.0]]
filters = []
for inter in intervals:
    a = list(filter(lambda x:(x>=inter[0] and x<=inter[1]),f_numbers))
    filters.append(a)
min_len = min(list(map(len,filters)))
final = []
for i in filters:
    j = i[:min_len]
    final.extend(j)
print(final)