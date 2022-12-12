class Number():
    def __init__(self, val, parents=[], op=None):
        self.val = val
        self.parents = parents
        self.children = []
        self.op = op
        self.grad = 0
    def get_op(self):
        return self.op
    def get_parents(self):
        return self.parents
    def get_children(self):
        return self.children
    def add_child(self, child):
        self.children.append(child)
    def clear_history(self):
        self.parents = []
        self.children = []
        self.op = []

    def __str__(self):
        out = f"VALUE: {self.val}\nParents: {self.parents}\nChildren: {self.children}\ngrad: {self.grad}\n"
        if self.op != None:
            out += str(self.op)
        return out
        

