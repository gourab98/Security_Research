def odd_numbers(x,y):
    return [n for n in range(x,y) if n%2!=0]

print(odd_numbers(5,15))