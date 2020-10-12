def get_count(input_str):
    num_vowels = 0
    val = 0
    vowel_arr = ['a', 'e', 'i', 'o', 'u']
    for element in vowel_arr:
        if element in input_str:
          val = input_str.count(element)
          num_vowels += val

    print(num_vowels)

get_count("abracadabra")