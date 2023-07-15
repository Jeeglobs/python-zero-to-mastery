# DEBUGGING

'''
* user linters to avoid syntax errors
* use an ide or editor (pycharm, etc.) to help detect errors
* learn to read errors
* use pdb (python debugger)
'''

import pdb


# pdb.set_trace() pauses the code and lets you interact with it in the terminal
# type help to see a list of commands
# type help <command> to see a tutorial on given command
def add(num1, num2):
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2


add(4, 'four')
