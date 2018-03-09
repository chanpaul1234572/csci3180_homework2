class Foo():
    def __init__(self):
        self.a = 1
    def s(self):
        print self.a
        return self.a
    def p(self):
        b = self.s()
        b += 1
        print b, self.a

f = Foo()
f.p()
