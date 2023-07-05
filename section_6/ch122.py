# @classmethod & @staticmethod

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    # decorater -> @classmethod
    # does not work w/o cls param
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Daniel', num1 + num2)

    '''
    @staticmethod works the same as @classmethod
    except that @staticmethod does not have access
    to cls
    '''
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)

# print(PlayerCharacter.adding_things(4, 5))

# player1 = PlayerCharacter('Tom', 20)

# print(player1.shout())

# print(player1.adding_things(2, 3))
