def tuple_func(Tuple):
    minimum_element = Tuple[0]
    for i in Tuple:
        if i < minimum_element:
            minimum_element = i
    print("Minimum element in given tuple is : ", minimum_element)




tuple_func((87, 78, 45, 34, 12, 4, 8, 9, 56, 100))