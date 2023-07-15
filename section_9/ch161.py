# EXERCISES: ERROR HANDLING

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
    finally:
        print('ok done')
