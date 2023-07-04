# HOC: HIGHER ORDER FUNCTIONS

# greet is an HOC
# a function that accepts another function as an argument
def greet(func):
    func()


# greet2 in an HOC
# a function that returns another function
def greet2():
    def func():
        return 5
    return func
