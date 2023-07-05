# UNDER THE HOOD OF GENERATORS

# what a for loop does basically
def for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


for_loop([1, 2, 3])


class Generator():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if Generator.current < self.last:
            num = Generator.current
            Generator.current += 1
            return num
        raise StopIteration


gen = Generator(0, 100)

for i in gen:
    print(i)
