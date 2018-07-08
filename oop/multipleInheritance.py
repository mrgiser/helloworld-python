class A:
    def __init__(self,name):
        self.name = name
        print("class A init")

    def hello(self, word):
        print("class A helloA " + word)

class B:
    def __init__(self,name2):
        self.name2 = name2
        print("class B init")

    def hello2(self,word):
        print("class B helloB " + word)

class C(A,B):
    def __init__(self,name):
        A.__init__(self,name)
        B.__init__(self,name)
        print('(C name: {})'.format(self.name))
        print('(C name2: {})'.format(self.name2))
    def hello(self,word):
        A.hello(self,word)
    def hello2(self,word):
        B.hello2(self,word)

c = C("HF")
c.hello("word")
c.hello2("word2")



