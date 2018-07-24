from util import time_class, time_function

@time_function
def printstuff():
    print("hi")

@time_function
def add(x, y):
    return x + y

printstuff()

rv = add(1, 2)
print(rv)

@time_class
class Foo(object):
    def hi(self):
        print("hi")

foo = Foo()

foo.hi()
