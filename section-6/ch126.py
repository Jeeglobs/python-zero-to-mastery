# ABSTRACTION

class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')


# abstraction -- only see what we need to?
print((1, 2, 3, 1).count(1))

player1 = PlayerCharacter('Daniel', 35)

player1.name = '!!!'
player1.speak = 'BOOOOO'

# prints BOOOOO
print(player1.speak)

# throws error b/c .speak() has been changed
print(player1.speak())
