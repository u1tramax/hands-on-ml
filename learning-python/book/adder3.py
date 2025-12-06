"""
Arbitrary arguments: Copy the file you wrote in the last exercise to adder2.py, generalize its adder
function to compute the sum of an arbitrary number of arguments, and change the calls to pass
more or fewer than two arguments. What type is the returned sum? (Hints: a slice such as S[:0]
returns an empty sequence of the same type as S, and the type built-in function can test types; but
see the manually coded min examples in Chapter 18 for a simpler approach.) What happens if you
pass in arguments of different types? What about passing in dictionaries?
"""

def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@printer
def adder(red=255, green=255, blue=255):
    return (red, green, blue)

adder(0, 0, 0)
adder(100, blue=100)
adder(10, green=100)
adder(blue=1, red=2)
