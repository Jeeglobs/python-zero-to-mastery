# DECORATORS 2

# decorators are functions that wrap other functions and enhance them

# def hello():
#     print('hello')


def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorator
def hello():
    print('hello')


hello()

hello2 = my_decorator(hello)
hello2()
