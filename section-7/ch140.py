# PURE FUNCTIONS

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))

'''
this is a pure function
every time you enter [1, 2, 3] you will get [2, 4, 6]
it does not interact with the 'outside world'

the versions below are NOT pure functions
they DO interact with the 'outside world'
'''

# # this interacts with print when called
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return print(new_list)


# multiply_by2([1, 2, 3])


# # this interacts with a list in the 'outside world'
# new_list = []
# def multiply_by2(li):

#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by2([1, 2, 3]))
