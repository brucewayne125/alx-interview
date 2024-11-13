#!/usr/bin/python3
def validUTF8(data):
    number_in_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if number_in_bytes == 0:
            if(byte & mask1) == 0:
                continue
            elif(byte & (mask1 >> 1)) == mask1:
                number_in_bytes = 1
            elif(byte & (mask1 >> 2)) == (mask1 >> 1):
                number_in_bytes = 2
            elif(byte & (mask1 >> 3)) == (mask1 >> 2):
                number_in_bytes = 3
            else:
                return False
        else:
            if not(byte & mask1 and not (byte & mask2)):
                return False
            number_in_bytes -= 1
    
    return number_in_bytes == 0
