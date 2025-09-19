from adder1 import printer

"""
Dictionary tools: Write a function called copyDict(dict) that copies its dictionary argument. It
should return a new dictionary containing all the items in its argument. Use the dictionary keys
method to iterate (or step over a dictionary’s keys without calling keys). Copying sequences is easy
(X[:] makes a top-level copy); does this work for dictionaries, too? As explained in this exercise’s
solution, because dictionaries come with similar tools, this and the next exercise are just coding
exercises but still serve as representative functions.
"""

def copyDict(dict):
    dict_copy = {}
    for k, v in dict.items():
        dict_copy[k] = v
    return dict_copy

"""
Dictionary tools: Write a function called addDict(dict1, dict2) that computes the union (i.e.,
merge) of two dictionaries. It should return a new dictionary containing all the items in both its
arguments (which are assumed to be dictionaries). If the same key appears in both arguments, feel
free to pick a value from either. Test your function by writing it in a file and running the file as a
script. What happens if you pass lists instead of dictionaries? How could you generalize your function
to handle this case, too? (Hint: see the type built-in function used earlier.) Does the order of
the arguments passed in matter? Dictionary merge is also a built-in today (actually, several), but
you’re trying to stretch yourself a bit by coding it manually.
"""

def addDict(dict1, dict2):
    dict3 = {}
    for k1, v1 in dict1.items():
        dict3[k1] = v1
    for k2, v2 in dict2.items():
        if k2 in dict3:
            continue
        else:
            dict3[k2] = v2
    return dict3

dict1 = {
    '1': 10,
    '2': 15,
    '4': 20,
    '6': 30
}

dict2 = {
    '2': 20,
    '3': 25,
    '5': 30,
    '6': 35
}

# print(addDict(dict1, dict2))

"""
More argument-matching examples: First, define the following six functions (either interactively or
in a module file that can be imported):
def f1(a, b): print(a, b) # Normal args
def f2(a, *b): print(a, b) # Positional collectors
def f3(a, **b): print(a, b) # Keyword collectors
def f4(a, *b, **c): print(a, b, c) # Mixed modes
def f5(a, b=2, c=3): print(a, b, c) # Defaults
def f6(a, b=2, *c): print(a, b, c) # Defaults and positional collectors
Now, test the following calls interactively, and try to explain each result; in some cases, you’ll probably
need to fall back on the matching rules covered in Chapter 18. Do you think mixing matching
modes is a good idea in general? Can you think of cases where it would be useful?
>>> f1(1, 2)
>>> f1(b=2, a=1)
>>> f2(1, 2, 3)
>>> f3(1, x=2, y=3)
>>> f4(1, 2, 3, **dict(x=2, y=3))
>>> f5(1)
>>> f5(1, 4)
>>> f5(1, c=4)
>>> f6(1)
>>> f6(1, *[3, 4])
"""

def f1(a, b): print(a, b) # Normal args
def f2(a, *b): print(a, b) # Positional collectors
def f3(a, **b): print(a, b) # Keyword collectors
def f4(a, *b, **c): print(a, b, c) # Mixed modes
def f5(a, b=2, c=3): print(a, b, c) # Defaults
def f6(a, b=2, *c): print(a, b, c) # Defaults and positional collectors

"""
Primes revisited: Recall the following code snippet from Chapter 13, which simplistically determines
whether a positive integer is prime:
x = num // 2 # For some num > 1, start at half
while x > 1:
if num % x == 0: # Remainder 0? Factor found
print(num, 'has factor', x)
break # Exit now and skip else
x -= 1
else: # Normal exit, when x reaches 1
print(num, 'is prime')
Package this code as a reusable function in a module file (num should be a passed-in argument),
and add some calls to the function at the bottom of your file to test. While you’re at it, experiment
with replacing the first line’s // operator with / to see how true division breaks this code (refer
back to Chapter 5 if you need a reminder). What can you do about negatives, and the values 0 and
1? How about speeding this up? Your outputs should look something like this:
Test Your Knowledge: Part IV Exercises | 555
13 is prime
13.0 is prime
15 has factor 5
15.0 has factor 5.0
"""

def prime(num):
    x = num // 2
    while x > 1:
        if num % x == 0: # Remainder 0? Factor found
            print(num, 'has factor', x)
            break # Exit now and skip else
        x -= 1
    else: # Normal exit, when x reaches 1
        print(num, 'is prime')

"""
Iterations and comprehensions: Write code to build a new list containing the square roots of all the
numbers in this list: [2, 4, 9, 16, 25]. Code this as a for loop first, then as a map call, then as a
list comprehension, and finally as a generator expression. Use the sqrt function in the built-in
math module to do the calculation (i.e., import math and say math.sqrt(X)). Of the four, which
approach do you like best?
"""

from math import sqrt
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Time estimated: {time.time() - start}')
        return result
    return wrapper

@timer
@printer
def squares1(l):
    result = []
    for elem in l:
        result.append(sqrt(elem))
    return result

@timer    
@printer
def squares2(l):
    return [sqrt(elem) for elem in l]

@printer
@timer
def squares3(l):
    return list(map(sqrt, l))

@printer
@timer
def squares4(l):
    for i in range(len(l)):
        yield sqrt(l[i])

"""
Timing tools: In Chapter 5, we saw three ways to compute square roots: math.sqrt(X), X ** .5,
and pow(X, .5). If your programs run a lot of these, their relative performance might become
important. To see which is quickest, use the timer2.py module (Example 21-7) we wrote in this
chapter to time each of these three tools. Use its bestoftotal function to test. Which of the three
square root tools seems to run fastest on your device and Python in general? Finally, how might
you use timer2.py to interactively time the speed of dictionary comprehensions versus for loops?
What about comprehensions with if clauses and nested for loops?
"""



"""
Recursive functions: Write a simple recursion function named countdown that prints numbers as it
counts down to zero. For example, a call countdown(5) will print: 5 4 3 2 1 stop. There’s no
obvious reason to code this with an explicit stack or queue, but what about a nonfunction
approach? Would a generator make sense here?
"""

def countdown(a):
    if a == 0:
        print('stop')
        return a
    else:
        print(a)
        return countdown(a - 1)
    
"""
Computing factorials: Finally, a computer-science classic (but demonstrative nonetheless). We
employed the notion of factorials in Chapter 20’s coverage of permutations: N!, computed as
N*(N-1)*(N-2)*...1. For instance, 6! is 6*5*4*3*2*1, or 720. Code and time four functions that,
for a call fact(N), each return N!. Code these four functions (1) as a recursive countdown per
Chapter 19; (2) using the functional reduce call per Chapter 19; (3) with a simple iterative counter
loop per Chapter 13; and (4) using the math.factorial library tool per Chapter 20. Use this chapter’s
timeit to time each of your functions. What conclusions can you draw from your results?
"""