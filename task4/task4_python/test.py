class Foo():
    __a = 2
    def __init__(self):
        self.b = Foo.__a
    def p(self):
        print self.b

f = Foo()
f.p()
