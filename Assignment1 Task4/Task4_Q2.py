# ii. Given an input n, count the total number of digit 1 appearing in all nonnegative integers less than or equal to n.
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

number = int(input("enter a number : "))
count = 0
for i in range(1, number+1):
    count += str(i).count("1")
print(count)
