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


def lastTwoSymb(stroka):
    return (stroka[-2:] == '1A' or stroka[-2:] == '1F')

def mod5and9(num):
    return ((num % 5 != 0) and (num % 9 != 0))



array = []


for i in range(2495, 7083 + 1):
    if lastTwoSymb(from10to16(i)):
        if mod5and9(i):
            array.append(i)
print(len(array))
print(min(array))