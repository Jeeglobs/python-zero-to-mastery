# OBJECT INSTROPECTION

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left: {self.num_arrows}')


# instropection
wizard1 = Wizard('Merlin', 60, 'merling@gmail.com')

# dir()
# shows all methods and attributes that the instance has
print(dir(wizard1))
