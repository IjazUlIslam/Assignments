# 3. Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically. Suppose the
# following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

input_string = str(input("enter your string : "))
word = input_string.split(",")
sort_word = sorted(word)
sorted_sequence = "," .join(sort_word)
print(sorted_sequence)
