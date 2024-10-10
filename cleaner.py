def string_cleaner(text): 
    '''

    '''
    result = '' # an empty string
    for character in text:
        #print(character)

        if character.isalpha():
            result += character.lower()

    return result

value = string_cleaner('HE 00 l L o!')

print(f"Value is: {value}")