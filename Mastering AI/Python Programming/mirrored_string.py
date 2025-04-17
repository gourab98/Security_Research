
def mirrored_string(my_string):
    forward = ""
    backward = ""

    for character in my_string:
        if character.isalpha():
                forward = forward + character
                backward = character + backward
        
    print(forward)
    print(backward)
    if forward.lower()==backward.lower():
         return True
    return False


print(mirrored_string("12 Noon")) 
print(mirrored_string("Was it a car or cat I saw"))
print(mirrored_string("'eve, Madam Eve"))