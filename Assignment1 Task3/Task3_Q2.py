integer_number = int(input("Enter your integer number : "))
my_dictionary = {}
for i in range(1, integer_number + 1):
    my_dictionary[i] = i * i
print(my_dictionary)