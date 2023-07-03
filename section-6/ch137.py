# MRO: METHOD RESOLUTION ORDER

# class A:
#     num = 10


# class B(A):
#     # num = 2
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.num)

# # shows MRO for D class
# print(D.mro())


'''

    A
   / \
  /   \
 B     C
  \   /
   \ /
    D

print(D.num)
checks D, then B, then C, then A
prints the first num it sees

'''


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


'''
MRO Guesses:
M, B, A, Z, Y, Z, X, object
M, B, Y, Z, A, X, Y, Z, object
'''

print(M.mro())
print(M.__mro__)

'''
Correct MRO:
M, B, A, X, Y, Z, object

why does it not start w/ M, B, A, Z?
-> Depth First Search
'''
