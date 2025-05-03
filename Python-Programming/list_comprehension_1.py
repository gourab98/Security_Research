# For loop:
multiple = []
for x in range(1,11):
    multiple.append(x*7)
print(multiple)

# List comprehensions:
multiple_1 = [ x*7 for x in range(1,11)]
print(multiple_1)

# List comprehensions 1:
languages = ["Python", "C++", "Perl", "Java", "Go", "Ruby", "R"]
length = [len(language) for language in languages]
print(length)

# List comprehensions 2:
z = [x for x in range(1,101) if x%3==0]
print(z)