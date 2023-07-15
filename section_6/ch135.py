# EXERCISE: EXTENDING LIST

class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
print(super_list1)

super_list1.append(5)
print(super_list1)
print(super_list1[0])

print(issubclass(SuperList, list))
print(issubclass(list, object))


'''
adding list to SuperList() makes SuperList inherit all of the attributes of list
now we can append SuperList
'''
