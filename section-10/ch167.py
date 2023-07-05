# EXERCISE: FIBONACCI NUMBERS


# n is F(n) in the fibonacci sequence
# generator is more memory efficient
def fib(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(20):
    print(x)


# using a list here is more taxing on memory
def fib2(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(30))
