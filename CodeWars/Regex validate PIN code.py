def validate_pin(pin):
    if len(pin) > 0 and pin.isnumeric():
        if len(pin) == 4 or len(pin) == 6:
           return True
        else:
            return False






x = validate_pin("1")
print(x)