
def from10to8(num):
    stroka = ''
    while (num != 0):
        stroka += str(num % 8)
        num //= 8
    return int(stroka[::-1])


def bliti(num):
    num8 = from10to8(num)
    num10 = num
    return len(str(num8)) != len(str(num10))




def from10to16(num):
    stroka = ''
    while (num != 0):
        if (num % 16) == 15:
            stroka += 'F'
        elif (num % 16) == 14:
            stroka += 'E'
        elif (num % 16) == 13:
            stroka += 'D'
        elif (num % 16) == 12:
            stroka += 'C'
        elif (num % 16) == 11:
            stroka += 'B'
        elif (num % 16) == 10:
            stroka += 'A'
        else:
            stroka += str(num % 16)
        num //= 16

    return stroka[::-1]
