# INHERITANCE 2

class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left: {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)

# isinstance(instance, Class)
print(isinstance(wizard1, Wizard))

# Wizard is a sub-class of User, so wizard1 is an instance of User
print(isinstance(wizard1, User))

# everything in python inherits from the base object class
print(isinstance(wizard1, object))
