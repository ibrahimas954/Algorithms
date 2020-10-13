def DNA_strand(dna):
    ret_arr = []
    if len(dna) > 0:
        for element in dna:
            if element == 'A':
                ret_arr.append('T')
            if element == 'T':
                ret_arr.append('A')
            elif element == 'G':
                ret_arr.append('C')
            elif element == 'C':
                ret_arr.append('G')

    new_arr = ''.join(ret_arr)
    return new_arr

##Short Way##
def DNA_strand(dna):
    keys = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([keys[i] for i in dna])


print(DNA_strand("AAAA"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))