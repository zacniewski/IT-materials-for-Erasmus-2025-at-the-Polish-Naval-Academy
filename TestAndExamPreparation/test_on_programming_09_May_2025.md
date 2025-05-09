#### I. Find the factorial of a given number

Write a `factorial()` function and use `for` loop inside it to find the factorial of a given number.

The factorial (symbol: `!`) means multiplying all numbers from the chosen number down to 1.

For example, a factorial of `5!` is 5 × 4 × 3 × 2 × 1 = 120

```python
def factorial(number):
    # your code here


print(factorial(5))
# it should print 120
```

> Hint: Create a variable to save the result of current multiplication.
> Every number multiplied by 1 gives this number, e.g. `5 x 1 = 5`

<br>

#### II. Reverse a integer number

Write a `reverse_int()` function and use `for` loop inside it to reverse the given integer.  

```python
def reverse_int(number):
    # your code here


print(reverse_int(76542))
# it should print 24567
```

> If you cast integer to string, then you can access every chcaracter in the string and do `for` loop on it.  
> `str(123) = '123'`


<br>


#### III. Find largest and smallest digit in a number

Write a `find_largest()` function that identifies the digit with the highest value and the digit with the lowest value within that number.

```python
def find_largest(number):
    # your code here


print(find_largest(19865))
# it should print 9
```

> Hint: `list("1234") = ['1', '2', '3', '4']`


<br>


#### IV. Calculate the sum and average of the digits present in a string

Write a `sum_of_digits()` function to return the sum of the digits that appear in the string, ignoring all other characters.  

```python
str1 = "ErasmUS29@#2025"

def sum_of_digits(string):
    # your code here


print(sum_of_digits(str1))
# it should print 20, because 2 + 9 + 2 + 0 + 2 + 5 = 20
```

> Hint: use `isdigit()` method for strings.  
> Use `for` loop on the string.  


<br>


#### V. Turn every item of a list into its square  
Write a `make_square()` function  to turn every item of a list into its square. 

```python
numbers = [1, 2, 3, 4, 5, 6, 7]

def make_square(numbers):
    # your code here


print(make_square(numbers))
# it should print [1, 4, 9, 16, 25, 36, 49]
```

> Hint: use `for` loop on every list element