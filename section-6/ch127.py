# PRIVATE VS PUBLIC VARIABLES

'''
private variable:
* we don't want people to be able to redefine certain variables such as __init__ attributes
* there is no true way to make variables 'private' in python
* the convention is to name a variable _var to tell programmers that this should not be changed
* __dunder__ methods also should not be modified
'''


class PlayerCharacter:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name}, and I am {self._age} years old.')


player1 = PlayerCharacter('Daniel', 35)

player1.name = '!!!'
player1.speak = 'BOOOOO'

# print(player1.speak())
print(player1.speak)
