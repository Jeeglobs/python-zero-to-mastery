#  USEFUL MODULES 2

import datetime
from array import array

print(datetime.time())
print(datetime.time(5, 45, 2))
print(datetime.date.today())


# use arrays when lists get very large and you do not want to use generators
arr = array('i', [1, 2, 3])

print(arr)
print(arr[0])
