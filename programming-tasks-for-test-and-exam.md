## Exercises aimed to prepare for programming test and exam
> Write  every solution in a single file called with the number of exercise and your surname, e.g. `exercise2_zacniewski.py`  
> After test and exam everybody will be asked some questions related to the given exercise and requested to do some little modifications of the programs !!!

#### Exercise 1
Write a program named that prompts the user for input with the string "Tell me your password:".  
The program should then determine the first letter of the user’s input, convert that letter to uppercase, and display it back.
For example, if the user input is "no", then the program should display
the following output:
>The first letter you entered was: N

<br>

#### Exercise 2
Create a string containing an integer, then convert that string into
an actual integer object using `int()`. Test that your new object is
a number by multiplying it by another number and displaying the
result.

<br>

#### Exercise 3
Print the result of fraction calculation (for example `2 / 10`) as a percentage with no decimal places.
The output should look like `20%` in the aforementioned case.


<br>

#### Exercise 4
Create a string object and an integer object, then display them side
by side with a single print function call using `str()`.

<br>

#### Exercise 5
Write a program that uses `input()` twice to get two numbers from
the user, multiplies the numbers together, and displays the result.
If the user enters 2 and 4, then your program should print the
following text:
> The product of 2 and 4 is 8.0.

<br>

#### Exercise 6
Write a program that asks the user for some input
with the following prompt: `Enter some text:`
Use `.replace()` to convert the text entered by the user into leetspeak
by making the following changes to lowercase letters:  
  - The letter a becomes 4
  - The letter b becomes 8
  - The letter e becomes 3
  - The letter l becomes 1
  - The letter o becomes 0
  - The letter s becomes 5
  - The letter t becomes 7
Your program should then display the resulting string as output. Below is a sample run of the program:
>Enter some text: I like to eat eggs and spam.  
>I 1ik3 70 347 3gg5 4nd 5p4m.  
 
<br>

#### Exercise 7

Write a program called exponent.py that receives two numbers from the
user and displays the first number raised to the power of the second
number.
Here’s sample run of what the program should look like, including
example input from the user:  
> Enter a base: 1.2  
> Enter an exponent: 3  
> 1.2 to the power of 3 = 1.7279999999999998

<br>

#### Exercise 8
Write a program that asks the user to input a number and then
displays that number rounded to two decimal places. When run,
your program should look like this:
>Enter a number: 5.432  
>5.432 rounded to 2 decimal places is 5.43  

<br>

#### Exercise 9
Write a program that asks the user to input a number and then
displays the absolute value of that number. When run, your
program should look like this:  
> Enter a number: -10  
> The absolute value of -10 is 10.0

<br>

#### Exercise 10
Write a program that asks the user to input two numbers by using
`input()` twice, then displays whether the difference between those
two numbers is an integer. When run, your program should look
like this:  
> Enter a number: 1.5  
>  Enter another number: .5  
> The difference between 1.5 and .5 is an integer? True!  

If user inputs two numbers whose difference is not integral,
then the output should look like this:  
> Enter a number: 1.5  
> Enter another number: 1.0  
> The difference between 1.5 and 1.0 is an integer? False! 

<br>

#### Exercise 11
Write a function called `cube()` that takes one number parameter
and returns the value of that number raised to the third power.
Test the function by calling your `cube()` function on a few different
numbers and displaying the results.  

<br>

#### Exercise 12
Write a function called `greet()` that takes one string parameter
called name and displays the text `"Hello <name>!"`, where `<name>` is
replaced by the value of the name parameter.  

<br>

#### Exercise 13
Write a program that defines two functions:
  - `convert_cel_to_far()`, which takes one float parameter representing degrees Celsius and returns 
a float representing the same temperature in degrees Fahrenheit using the following formula:
F = C * 9/5 + 32
  - `convert_far_to_cel()`, which takes one float parameter representing degrees Fahrenheit and returns a float representing the same
temperature in degrees Celsius using the following formula:
C = (F - 32) * 5/9  
The program should do the following:

1. Prompt the user to enter a temperature in degrees Fahrenheit and
then display the temperature converted to Celsius
2. Prompt the user to enter a temperature in degrees Celsius and then
display the temperature converted to Fahrenheit
3. Display all converted temperatures rounded to two decimal places  
Here’s a sample run of the program:  
```
Enter a temperature in degrees F: 72
72 degrees F = 22.22 degrees C

Enter a temperature in degrees C: 37
37 degrees C = 98.60 degrees F
```

<br>

#### Exercise 14
Write a `for` loop that prints out the integers from 2 to 10, each on
a new line, using `range()`.

<br>

#### Exercise 15
Write a `while` loop that prints out the integers from 2 to 10. 
> Hint: You’ll need to create a new integer first.

<br>

#### Exercise 16
Write a function called `doubles()` that takes a number as its input
and doubles it. Then use `doubles()` in a loop to double the number `2`
three times, displaying each result on a separate line. Here’s some
sample output:  
```
4
8
16
```

<br>

#### Exercise 17
For each of the following expressions, fill in the blank (indicated by
__) with an appropriate Boolean comparator so that the expression
evaluates to `True`:
  3 __ 4  
  10 __ 5  
  "jack" __ "jill"  
  42 __ "42"  
> For example `print(1 == 1)` gives `True`, etc.

<br>

#### Exercise 18
Write a program that prompts the user to enter a word using the
input() function and compares the length of the word to the number five. 
The program should display one of the following outputs,
depending on the length of the user’s input:
  • "Your input is less than 5 characters long"
  • "Your input is greater than 5 characters long"
  • "Your input is 5 characters long"  

<br>

#### Exercise 19
Write a program that displays "I'm thinking of a number between 1
and 10. Guess which one." Then use `input()` to get a number from
the user. If the user inputs the number 3, then the program should
display "You win!" For any other input, the program should display
"You lose."  

<br>

#### Exercise 20
Write a program that asks the user to input a positive integer and then prints out the factors of that number. 
Here’s a sample run of the program with output:  
```
Enter a positive integer: 12
1 is a factor of 12
2 is a factor of 12
3 is a factor of 12
4 is a factor of 12
6 is a factor of 12
12 is a factor of 12
```

>Hint: You can use the % operator to get the
remainder of dividing one number by another.

<br>

#### Exercise 21
1. Create a tuple literal named `cardinal_numbers` that holds the strings
"first", "second", and "third", in that order.  
2. Using index notation and `print()`, display the string at index 1 in
`cardinal_numbers`.  
3. In a single line of code, unpack the values in `cardinal_numbers` into
three new strings named `position1`, `position2`, and `position3`. Then
print each value on a separate line.  
4. Using `tuple()` and a string literal, create a tuple called `my_name` that
contains the letters of your name.  
5. Check whether the character "a" is in `my_name` using the `in` keyword.  
6. Create a new tuple containing all but the first letter in `my_name` using
slice notation.  

<br>

#### Exercise 22
1. Create a list named food with two elements, "rice" and "beans".  
2. Append the string "broccoli" to food using `.append()`.    
3. Add the strings "bread" and "pizza" to food using `.extend()`.  
4. Print the first two items in the food list using `print()` and slice notation.  
5. Print the last item in food using `print()` and index notation.  
6. Create a list called `breakfast` from the string "eggs, fruit, orange
juice" using the string `.split()` method.  
7. Verify that breakfast has three items using `len()`.

<br>

#### Exercise 23
1. Create an empty dictionary named `captains`.  
2. Using square bracket notation, enter the following data into the
dictionary one item at a time:  
  'Enterprise': 'Picard'  
  'Voyager': 'Janeway'  
  'Defiant': 'Sisko'  
3. Write two `if` statements that check if "Enterprise" and "Discovery"
exist as keys in the dictionary. Set their values to "unknown" if the
key does not exist.  
4. Write a `for` loop to display the ship and captain names contained
in the dictionary. For example, the output should look something
like this:  

```
The Enterprise is captained by Picard.
```

5. Delete "Discovery" from the dictionary.

<br>

#### Exercise 24
The following code defines a function `add_underscores()` that takes a
single string object word as an argument and returns a new string containing a copy of word with each character surrounded by underscores.
For example, `add_underscores("python")` should return `"_p_y_t_h_o_n_"`.  

Here’s the buggy code:  
```python
def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word = word[i] + "_"
    return new_word

phrase = "hello"
print(add_underscores(phrase))
```

Run the program. The expected output is `_h_e_l_l_o_`, but instead
all you see is `o_`, or the letter `"o"` followed by a single underscore.  
Please, fix it!  


