def alphabet_position(text):
    plaintext = dict('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    text = text.replace(' ','')
    let_arr = []
    numbers = []

    for letter in text.upper():
        let_arr.append(letter)
    print(let_arr)


alphabet_position("The sunset sets at twelve o' clock.")
text = "sunset sets at twelve o clock."
text.replace(' ','')
print(text)