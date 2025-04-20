def add_one(number):
    return number+1

numbers = [1,2,3,4,5]

result = map(add_one,numbers)
print(list(result))
