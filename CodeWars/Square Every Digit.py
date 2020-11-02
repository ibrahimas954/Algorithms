def square_digits(num):
    retr_val = ''
    for element in str(num):
        retr_val = retr_val + str(int(element) ** 2)
    return int(retr_val)
        