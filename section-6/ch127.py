# PRIVATE VS PUBLIC VARIABLES

class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')


player1 = PlayerCharacter('Daniel', 35)

player1.name = '!!!'
player1.speak = 'BOOOOO'
