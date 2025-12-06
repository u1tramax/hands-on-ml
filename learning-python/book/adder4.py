"""
Keywords: In an adder3.py, change the adder function from exercise 2 to accept and sum/concatenate
three arguments: def adder(red, green, blue). Now, provide default values for each argument,
and experiment with calling the function interactively or code tests in the file. Try passing
one, two, three, and four arguments. Then, try passing keyword arguments. Does the call
adder(blue=1, red=2) work? Why? Finally, copy and generalize the new adder to accept and
sum/concatenate an arbitrary number of keyword arguments in an adder4.py. This is similar to
what you did in exercise 3, but you’ll need to iterate over a dictionary, not a tuple. (Hint: the
dict.keys method returns an iterable you can step through with a for or while, but be sure to
wrap it in a list call to index it; dict.values may help here too.)
"""

def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@printer
def adder(**kwargs):
    result = []
    for k, v in kwargs.items():
        result.append(v)
    return result

hash = {
    '1': 'abc',
    '2': 'def'
}
adder(**hash)