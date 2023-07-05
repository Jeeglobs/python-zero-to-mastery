# POLYMORPHISM

class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left: {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

# uses attack method in Wizard Class, not attack method in User Class
# if you add User.attack in Wizard attack method (line 17):
print(wizard1.attack())


def player_attack(char):
    char.attack()


'''
the same function gives a different output b/c of the object we are passing in it
this is polymorphism
'''

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
