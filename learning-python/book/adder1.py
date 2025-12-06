"""
The basics: At the Python interactive prompt, write a function named echo that prints its single
argument to the screen and call it interactively, passing a variety of object types: string, integer, list,
dictionary. Then, try calling it without passing any argument. What happens? What happens when
you pass two arguments?
"""

def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@printer
def adder(a, b):
    return a + b

adder('abc', 'def')
adder([1, 2, 4], [4, 5, 1])
adder(1.0, 2.0)