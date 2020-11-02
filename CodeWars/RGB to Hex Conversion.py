def rgb(r, g, b):

    def convertHex(val):
        if val <= 0:
            return "00"
        elif val >= 255:
            return "FF"
        else:
            return str('%02x' % val)

    hex_red = convertHex(r)
    hex_green =  convertHex(g)
    hex_blue =  convertHex(b)
    hex_return = hex_red + hex_green + hex_blue
    return str(hex_return.upper())

        
       

print(rgb(1,2,3))