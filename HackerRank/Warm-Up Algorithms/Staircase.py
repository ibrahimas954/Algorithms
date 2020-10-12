
i = 1
number = int(input("Ne kadar uzunlukta olsun ?"))

for i in range(number + 1):
    space = ' ' * (number - i)
    hash = '#' * i
    print(space + hash)