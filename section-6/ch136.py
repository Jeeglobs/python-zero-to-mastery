# MULTIPLE INHERITANCE

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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

    def run(self):
        print('ran really fast')


# We want HybridBorg to have access to all the methods of Wizard AND Archer
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb1 = HybridBorg('borgie', 50, 100)

'''
('borgie', 50) -> (name, power)
HybridBorg inherits from Wizard first -> needs name & power to instantiate
check_arrows() doesn't work b/c we never passed arrows
add Archer.__init__ method to HybridBorg to get arrows
now have to do the same for Wizard.__init__ to get attack
'''

print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
print(hb1.sign_in())
