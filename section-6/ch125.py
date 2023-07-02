# ENCAPSULATION

class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')


# name and age are encapsulated
player1 = PlayerCharacter('Daniel', 35)
player1.speak()

'''
wihtout methods, the class is the same
as a dictionary. it just changes how you
call the information
'''

player2 = {
    'name': 'Daniel',
    'age': 35,
}

print(player1.name)
print(player1.age)

print(player2['name'])
print(player2['age'])
