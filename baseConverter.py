import math
import string

# def numToBase(n, b):
#     conversion_table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     if b > len(conversion_table): raise ValueError
#     digits = ''
#     while n:
#         digits += conversion_table[n % b]
#         n //= b
#     return digits[::-1]

def numToBase(num, base, numBase=10, precision=0):
    # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    symbols = string.digits + string.ascii_uppercase

    # if num is a string, float, int, whatever: turn it into a float
    num = float(num)

    # get rid of the weird precision stuff
    num = round(num, precision + 1)

    # if num is in a base other than 10, first convert it to base 10
    if numBase != 10:
        num = float(num, numBase)

    # if the base is larger than the symbols allow for, Dont
    if base > len(symbols): raise ValueError

    # get the amount of digits in the whole part of the number
    if num == 0:
        return '0.0'
    
    digitCount = math.log(num, base)

    if (digitCount < 0):
        digitCount = math.ceil(digitCount)
    else:
        digitCount = math.floor(digitCount)

    digitString = ''

    if (digitCount < 0):
        digitString = '0.'
        for i in range(-digitCount):
            digitString += '0'

    for i in range(-digitCount, precision):
        digitString += symbols[int(num * base ** i) % base]
        if i == 0:
            if precision > 0:
                digitString += '.'
            else:
                break


    if digitString == '':
        return 'whoops'

    return str(float(digitString))