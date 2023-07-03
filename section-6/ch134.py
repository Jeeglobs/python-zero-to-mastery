# DUNDER METHODS

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    # redefine __str__
    def __str__(self):
        return f'{self.color}'

    # redefine __len__
    def __len__(self):
        return 5

    # redefine __del__
    def __del__(self):
        print('deleted')

    # redefine __call__
    def __call__(self):
        return 'yesss?'

    # redefine __getitem__
    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)

# do the same
print(action_figure.__str__())
print(str(action_figure))
print(action_figure)

'''
if you redefine __str__ in the Toy class,
__str__ changes only when called on that class
'''

print(str('action_figure'))
print(len(action_figure))
print(len('action_figure'))

# del action_figure

# call
print(action_figure())

print(action_figure['name'])
