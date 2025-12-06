"""
Arguments: Write a function called adder in a Python module file named adder1.py. The function
should accept two arguments and return the sum (or concatenation) of the two. Then, add code at
the bottom of the file to call the adder function with a variety of object types (two strings, two lists,
two floating points), and run this file as a script from the system command line. Do you have to
print the call statement results to see results on your screen?
"""

def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@printer
def adder(*args):
    count = 0
    first = None
    for elem in args:
        if count == 0:
            first = elem
            count += 1
        else:
            first += elem
    return first

adder('abc', 'def', 'ghijk')
adder([1, 2, 4], [4, 5, 1], [101, 1e10, -1])
adder(1.0, 2.0, -100.1)
# adder(1.0, 2.0, -100.1, '100', [1, 2])
adder({'a': 1, 'b': 2}, {'a': 10, 'b': 12})