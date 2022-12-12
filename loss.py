from Number import Number
from utils import topsort
from Ops import *

"""
Call Computes the loss between the label and the 
Backward will find the ordering to compute the gradients (top sort)
"""

class MSELoss():
    def __init__(self):
        self.loss = None
    def __call__(self, pred, label):
        loss = SUB.call(pred, label)
        loss = MULT.call(loss, loss)
        self.loss = loss

    def back(self):
        order = topsort(self.loss)
        order[0].grad = 1
        for i in range(len(order)):
            if len(order[i].parents) == 0:
                continue
            grad_dict = order[i].op.bprop()
            for ins in order[i].parents:
                ins.grad += (order[i].grad * grad_dict[ins].val)
        self.last = order

