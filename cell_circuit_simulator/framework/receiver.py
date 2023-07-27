from framework.cell import Cell

class Receiver(Cell):
    def __init__(self, signals_in, signal_out):
        super().__init__()
        self.inputs = {signal_in: False for signal_in in signals_in}
        self.outputs = {signal_out: False}
        self.signal_in = signals_in
        self.signal_out = signal_out
    
    #Sets outputs to True when both inputs IPTG and AHL are True
    def logic(self, recv_signals):
        for rs in recv_signals:
            self.inputs[rs] = True
        # Set output
        self.outputs[self.signal_out] = all(self.inputs[signal] for signal in self.signal_in)
