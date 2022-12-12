from Number import Number

##########################################################################################
#                                           BINARY OPS                                   # 
##########################################################################################
class ADD():
    def __init__(self, input1, input2):
        self.inputs = [input1, input2]
        self.output = None
        self.bprop = None
    def call(input1, input2):
        val = input1.val + input2.val
        op = ADD(input1, input2)
        output = Number(val, op.inputs, op)
        output.op = op
        input1.add_child(output)
        input2.add_child(output)
        def back():
            return {input1: Number(1), input2: Number(1)}
        op.bprop = back
        return output
    def __str__(self):
        out = f"ADDITION\ndout/din1: {self.bprop()[self.inputs[0]].val}\ndout/din2: {self.bprop()[self.inputs[1]].val}\n"
        return out

class SUB():
    def __init__(self, input1, input2):
        self.inputs = [input1, input2]
        self.output = None
        self.bprop = None
    def call(input1, input2):
        val = input1.val - input2.val
        op = SUB(input1, input2)
        output = Number(val, op.inputs, op)
        output.op = op
        input1.add_child(output)
        input2.add_child(output)
        def back():
            return {input1:Number(1), input2: Number(-1)}
        op.bprop = back
        return output
    def __str__(self):
        out = f"SUB\n{self.bprop()[self.inputs[0]].val}\ndout/din2: {self.bprop()[self.inputs[1]].val}\n"
        return out


class MULT():
    def __init__(self, input1, input2):
        self.inputs = [input1, input2]
        self.output = None
        self.bprop = None
    def call(input1, input2):
        val = input1.val * input2.val
        op = MULT(input1, input2)
        output = Number(val, op.inputs, op)
        input1.add_child(output)
        input2.add_child(output)
        def back():
            return {input1: input2, input2: input1}
        op.bprop = back
        return output
    def __str__(self):
        out = f"MULT\ndout/din1: {self.bprop()[self.inputs[0]].val}\ndout/din2: {self.bprop()[self.inputs[1]].val}\n"
        return out

class DIV():
    def __init__(self, input1, input2):
        self.inputs = [input1, input2]
        self.output = None
        self.bprop = None
    def call(input1, input2):
        val = input1.val / input2.val
        op = DIV(input1, input2)
        output = Number(val, op.inputs, op)
        input1.add_child(output)
        input2.add_child(output)
        def back():
            return {input1: input2, input2: input1}
        op.bprop = back
        return output
    def __str__(self):
        out = f"MULT\ndout/din1: {self.bprop()[self.inputs[0]].val}\ndout/din2: {self.bprop()[self.inputs[1]].val}\n"
        return out

###########################################################################################
#                                           UNARY OPS                                     #
###########################################################################################
class NEG():
    def __init__(self, input1):
        self.inputs = [input1]
        self.output = None
        self.bprop = None
    def call(input1):
        val =  -input1.val
        op = NEG(input1)
        output = Number(val, op.inputs, op)
        input1.add_child(output)
        def back():
            return {input1: Number(-1)}
        op.bprop = back
        return output
    def __str__(self):
        out = f"NEG\ndout/din1: {self.bprop()[self.inputs[0]].val}\n"
        return out

###########################################################################################
#                                       
