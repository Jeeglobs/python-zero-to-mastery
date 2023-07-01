# OOP

# # create a class
# class BigObject:
#     pass


# print(type(BigObject))

# # instanciate an object
# obj1 = BigObject()

# print(type(obj1))

class PlayerCharacter:
    # __init__ method: automatically called when object is instanciated
    def __init__(self, name, age):
        # self refers to PlayerCharacter
        self.name = name  # attributes
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Jeeglobs', 35)
player2 = PlayerCharacter('jangleJANGLE', 34)

print(player1)
print(player2)

print(player1.name, player1.age)
print(player2.name, player2.age)

print(player1.run())
