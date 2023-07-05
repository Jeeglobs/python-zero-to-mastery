# MAP()

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


def multiply_by2(item):
    return item * 2


print(multiply_by2([1, 2, 3]))

print(map(multiply_by2, [1, 2, 3]))
print(list(map(multiply_by2, [1, 2, 3])))
