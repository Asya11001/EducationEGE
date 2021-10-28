

# Рассматривается множество целых чисел,
# принадлежащих числовому отрезку [1000; 9999],
# запись которых в пятеричной системе имеет
# не менее 6 цифр и заканчивается на 21 или 23.
# Найдите количество таких чисел и минимальное из них.

def from10to5(num):
    stroka = ''
    while (num != 0):
        stroka += str(num % 5)
        num //= 5
    return int(stroka[::-1])
def NotLess6Numb(num):
    return len(str(num)) >= 6
def mod21(num):
    return ((num % 10 == 1) and ((num // 10) % 10 == 2))
def mod23(num):
    return ((num % 10 == 3) and ((num // 10) % 10 == 2))


array = []
for i in range(1000, 9999 + 1):
    if NotLess6Numb(from10to5(i)):
        if (mod21(from10to5(i)) or mod23(from10to5(i))):
            array.append(i)

print(len(array))
print(min(array))


