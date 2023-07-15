# WORKING WITH FILES

my_file = open('section_12/ch_185/test.txt')

# prints file object
print(my_file)

# prints txt file
print(my_file.read())

# resets cursor to beginning of txt file
my_file.seek(0)
print(my_file.read())

my_file.seek(0)

# reads one line at a time
print(my_file.readline())

# returns a list of lines
print(my_file.readlines())

# closes file
my_file.close()
