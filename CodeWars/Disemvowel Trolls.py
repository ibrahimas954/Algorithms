def disemvowel(string):
    vowel_arr = ['a', 'e', 'i', 'u', 'o', 'E', 'I', 'U', 'O']
    new_string = string
    for element in string:
        if element in vowel_arr:
            new_string = new_string.replace(element, "")

    return new_string