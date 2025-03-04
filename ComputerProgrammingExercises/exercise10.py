def repeat(word, n):
    print(word * n)


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


to_check = absolute_value(-8)
print(to_check)



def is_divisible(x, y):
    return x % y == 0

# option 1
print(is_divisible(4, 2))

# option 2
check_divisible = is_divisible(6, 4)
print(check_divisible)