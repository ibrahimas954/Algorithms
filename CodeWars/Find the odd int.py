def find_it(seq):
    
    for element in seq:
        counter = seq.count(element)
        if counter%2 == 1:
            return element