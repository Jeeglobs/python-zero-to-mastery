# OOP

# # create a class
# class BigObject:
#     pass


# print(type(BigObject))

# # instanciate an object
# obj1 = BigObject()

# print(type(obj1))


class PlayerCharacter:
    # class object attribute--NOT dynamic
    membership = True

    # __init__ method: automatically called when object is instanciated
    def __init__(self, name='anonymous', age=0):
        # self refers to PlayerCharacter
        # checks to see if membership = True before instanciating
        if self.membership and age > 18:
            self.name = name  # attributes
            self.age = age

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f'My name is {self.name}')


player1 = PlayerCharacter('Jeeglobs', 35)
player2 = PlayerCharacter('jangleJANGLE', 15)

print(player1)
print(player2)

print(player1.name, player1.age)
print(player2.name, player2.age)

print(player1.run())

# help(player1)

print(player1.membership)

print(player1.shout())
