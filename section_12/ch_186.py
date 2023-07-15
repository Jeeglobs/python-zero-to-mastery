# READ, WRITE, APPEND

# # with allows us to read files without closing them afterwards
# # mode='r' is default, and reads files
# with open('section_12/ch_185/test.txt', mode='r') as my_file:
#     print(my_file.readlines())

# mode='w' lets us write (will overwrite anything previously in the file)
# mode='r+' lets us read AND write
# mode='a' lets us append
with open('section_12/ch_185/test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me!')
    print(text)

# can create files with mode='w'
with open('sad.txt', mode='w') as sad_file:
    text = sad_file.write('I\'m sad')
    print(text)
