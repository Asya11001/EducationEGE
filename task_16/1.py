




def pop(start, x):
    if x < start:
        return 0
    if x == start:
        return 1
    k = pop(start, x - 1)
    if x % 3 == 0:
        k += pop(start, x // 3)
    if x % 4 == 0:
        k += pop(start, x // 4)
    return k

print(pop(1, 5))
