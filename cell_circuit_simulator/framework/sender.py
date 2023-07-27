from framework.cell import Cell

class Sender(Cell):
    def __init__(self, signal_in, signal_out):
        super().__init__()
        self.inputs = {signal_in:False}
        self.outputs = {signal_out:False}
        self.signal_in = signal_in
        self.signal_out = signal_out

    def logic(self, recv_signals):
        # Add all inputs
        for rs in recv_signals:
            self.inputs[rs] = True
        # Update output
        self.outputs[self.signal_out] = self.inputs[self.signal_in]
