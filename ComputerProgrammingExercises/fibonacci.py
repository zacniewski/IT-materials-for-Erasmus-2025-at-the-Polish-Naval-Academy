import timeit


"""
    F(n) = F(n-1) + F(n-2)

    Where:
    F(0) = 0
    F(1) = 1
    F(n) for n > 1 is the sum of the two preceding numbers.
    
    We have:     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
"""


def fibonacci_recursion(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)



fib_array = [0, 1]


def fibonacci_dynamic(n):
    # Check is n is less than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is less than len(fib_array)
    elif n < len(fib_array):
        return fib_array[n]
    else:
        fib_array.append(fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2))
        return fib_array[n]


def fibonacci_memo(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
        return memo[n]


# your code
def precompute_fibonacci(n_max):
    fib = [0, 1]
    for i in range(2, n_max + 1):
        fib.append(fib[-1] + fib[-2])
    return fib[n_max]

#########################
# number to count
n = 2000

"""t1 = timeit.default_timer()
print("The number is: ", fibonacci_dynamic(n))
t2 = timeit.default_timer()
print(f"Fibonacci dynamic: {t2 - t1:.3f} seconds")"""

"""t1 = timeit.default_timer()
print("The number is: ", fibonacci_memo(n))
t2 = timeit.default_timer()
print(f"Fibonacci memo: {t2 - t1:.3f} seconds")"""


t1 = timeit.default_timer()
print("The number is: ", precompute_fibonacci(n))
t2 = timeit.default_timer()
print(f"Fibonacci precomputed: {t2 - t1:.3f} seconds")

# Very slow for higher number
# Uncomment if you want to check
# t1 = timeit.default_timer()
# print(fibonacci_recursion(n))
# t2 = timeit.default_timer()
# print(f"Fibonacci recursion: {t2 - t1:.3f} seconds")