# DECORATORS

# @classmethod
# @staticmethod

def hello():
    print('hello')


greet = hello

greet()

del hello

greet()

# print(hello())

'''
functions can act like variables
greet() still works after deleting hello
-> hello is removed from memory but greet still points to the hello function
'''


def goodbye(func):
    func()


def meet():
    print('nice to meet you!')


example = goodbye(meet)

print(example)
