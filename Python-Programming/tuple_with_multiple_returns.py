# Multiple value return:

def calculate_numbers(a,b):
    return a+b,a-b,a*b,a/b

result = calculate_numbers(10,5)
print(result)


# Catching a value from multiple return:

add_result, sub_result, mul_result, div_result = result
print(add_result)
print(sub_result)


