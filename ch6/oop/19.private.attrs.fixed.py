class A:
    def __init__(self, factor):
        self.__factor = factor  # note: Python에서는 name mangling에 의해서 name collision이 피할수 있도록 함

    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))

class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))

obj = B(100)
obj.op1()  # Op1 with factor 100...
obj.op2(42)  # Op2 with factor 42...
obj.op1()  # Op1 with factor 100...  <- Wohoo! Now it's GOOD!

print(obj.__dict__.keys())
# dict_keys(['_A__factor', '_B__factor'])
