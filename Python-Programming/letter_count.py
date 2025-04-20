def count_letter(text):
    result ={}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter]= result[letter] + 1
    return result

print(count_letter("Helloooooo"))