

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
count = 0
for i in range(1000, 9999 + 1):
    num = from10to5(i)
    if NotLess6Numb(num):
        if (mod21(num) or mod23(num)):
            array.append(i)

print(len(array))
print(min(array))


