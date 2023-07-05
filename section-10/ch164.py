# GENERATORS 2
# generators are iterable

def generator_function(num):
    for i in range(num):
        # yield pauses the function
        # yield i
        yield i * 2


# for item in generator_function(100):
#     print(item)


# print(generator_function(100))
g = generator_function(100)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


'''
generators use yield
yield pauses the function
next() resumes the function for one loop
will get error if you use next and you go past the range
'''
