# SUPER()

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


'''
a user enters an email before creating a character
we want to avoid having a user re-enter email when they create a wizard
call the User __init__ inside the Wizard __init__
super() makes the code cleaner
super() refers to User and we don't need to pass self
'''


class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
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


wizard1 = Wizard('Merlin', 60, 'merling@gmail.com')
# archer1 = Archer('Robin', 30)

print(wizard1.sign_in())
print(wizard1.email)
