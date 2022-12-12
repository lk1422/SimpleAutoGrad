from Number import Number
import random
from Ops import *

class Quadratic():
    def __init__(self):
        self.coeff = Number(random.random())
        self.coeff2 = Number(random.random())
        self.bias = Number(random.random())
        self.parameters = [self.coeff, self.coeff2, self.bias]
    def __call__(self, x):
        in_sqr = MULT.call(x, x)
        out1 = MULT.call(self.coeff, in_sqr)
        out2 = MULT.call(x, self.coeff2)
        out2 = ADD.call(out1,out2)
        out3 = ADD.call(out2, self.bias)
        return out3

