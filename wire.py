from cell import Cell

class Wire(Cell):
    def __init__(self, signal_in):
        super().__init__()
        self.inputs = {signal_in:False}
        self.outputs = {signal_in:False}
        self.signal_in = signal_in
        self.signal_out = signal_in

    #Forwards AHL signal
    def logic(self, recv_signals):
        for rs in recv_signals:
            self.inputs[rs] = True
        self.outputs[self.signal_out] = self.inputs[self.signal_in]
