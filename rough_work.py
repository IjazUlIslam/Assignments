# Define the size of the checkerboard
rows = 8
cols = 7

# Loop through rows
for i in range(rows):
    # Loop through columns
    for j in range(cols):
        # If the sum of the row and column indices is even, print "*", otherwise print a space
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    # Move to the next line after each row
    print()
