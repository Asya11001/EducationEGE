




def endsWith11(num):
    return (num % 2 == 1 and (num // 2) % 2 == 1)


def endsWith5(num):
    return num % 9 == 5

array = []
max_num = -1
for i in range(2807, 8558 + 1):
    if (endsWith11(i) and endsWith5(i)):
        if i > max_num:
            max_num = i
        array.append(i)


print(sum(array), max_num)

