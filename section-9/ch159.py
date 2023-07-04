# ERROR HANDLING

# # we want only int but this allows any input
# age = input('What is your age? ')
# print(age)


# this makes the input an int, but throws error if input is letters
# age = int(input('What is your age? '))
# print(age)


while True:
    try:
        age = int(input('what is your age? '))
        print(10/age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number higher than zero')
    else:
        print('thank you!')
        break
