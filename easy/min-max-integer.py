'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly 
four of the five integers. Then print the respective minimum and maximum values as a single line of two 
space-separated long integers
'''
'''
A single line of five space-separated integers

Sample Input
1 2 3 4 5

Sample Output
10 14
'''

# using list comprehension here
get_input = [int(x) for x in (raw_input("input 5 numbers").strip()).split()]
print get_input

sum = 0

for x in get_input:

	sum = sum + x
print sum