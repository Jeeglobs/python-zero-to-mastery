# ERROR HANDLING 2

# # print(sum('1', 2)) --> throws error
# def sum(num1, num2):
#     return num1 + num2


# def sum(num1, num2):
#     try:
#         return num1 + num2
#     # as err saves the error as an object
#     except TypeError as err:
#         print('please enter numbers')
#         print(err)


# print(sum('1', 2))


def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print('oops!')
        print(err)


print(sum(1, 0))
