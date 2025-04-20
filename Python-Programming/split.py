# Should print "one-1 two-2 three-3 four-4 five-5"

def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
    for element in new_list:
        new_string = new_string + element[1:] + "-" + element[0] + " "
    return new_string

print(change_string("1one 2two 3three 4four 5five")) 