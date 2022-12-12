from Number import Number
from function import *
from loss import *
from Ops import *
from optim import *



def train(function, loss, optim):
    target_function = [ (Number(i),Number((i**2)*5 + 2.3*(i) + 3)) for i in range(10)]
    for e in range(10000):
        for x,y in target_function:
            out = function(x)
            loss(out,y)
            loss.back()
            optim.step()
            optim.zero_grad()
            print(f.coeff.val, f.coeff2.val, f.bias.val)
            print(f"LABEL: {y.val}, PRED: {out.val}")
            print(loss.loss.val)
            x.clear_history()
            y.clear_history()




if __name__ == "__main__":
    f = Quadratic()
    optim = GradDescent(f.parameters,lr=.0001)
    loss = MSELoss()
    train(f,loss,optim)







