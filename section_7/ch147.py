# EXERCISE: LAMBDA EXPRESSIONS

'''
List Squaring:
create a lambda expression that will square my_list
should print [25, 16, 9]
'''

my_list = [5, 4, 3]

# print(lambda item: item ** 2, my_list)

print(list(map(lambda item: item ** 2, my_list)))


'''
List Sorting:
sort list a by the second value in each tuple
should print [(10, -1), (0, 2), (4, 3), (9, 9)]
'''

a = [(0, 2), (4, 3), (10, -1), (9, 9)]

a.sort(key=lambda x: x[1])
print(a)
