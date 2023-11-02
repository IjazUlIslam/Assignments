def solid_square(integer,character):
    for i in range(integer):
            print(character * integer)
solid_square(int(input("enter side length of square : ")), str((input("Enter character of square : "))))