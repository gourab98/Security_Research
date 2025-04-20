# Convert list in to tuple
my_list = [1,2,3,4,5,6]
my_tuple = tuple(my_list)
print(type(my_tuple), "Tuple : ", my_tuple)


# Creating tuple
tuple_list = 1,2,3,4,5
print(type(tuple_list), "Tuple list: ", tuple_list)


# Creating tuple 1
tuple_1 = (1,2,['a','b','c'])
tuple_1[2][1] = 'x'
print(type(tuple_1), 'Tuple_1: ', tuple_1)


# Creating tuple 2
tuple_1 = tuple(i for i in range(1,10,2))
print(tuple_1)
