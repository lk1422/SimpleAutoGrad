class GradDescent():
    def __init__(self, params, lr=.001):
        self.params = params
        self.lr = lr
    def step(self):
        for p in self.params:
            p.val -= self.lr*p.grad
    def zero_grad(self):
        for p in self.params:
            p.grad = 0
            p.clear_history()

        
