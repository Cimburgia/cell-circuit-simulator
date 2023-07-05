#!/usr/bin/env python
import sys

class Cell:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        self.from_cells = []
        self.to_cells = []
    
    def update(self, signals_in):
        self.logic(signals_in)
        for tc in self.to_cells:
            tc.update(self.outputs)

    def connect(self, cell):
        self.to_cells.append(cell)
        cell.from_cells.append(self)
        cell.update(self.outputs)
    
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
        

class Receiver(Cell):
    def __init__(self, signals_in, signal_out):
        super().__init__()
        self.inputs = {signal_in: False for signal_in in signals_in}
        self.outputs = {signal_out: False}
        self.signal_in = signals_in
        self.signal_out = signal_out
    
    def logic(self, recv_signals):
        for rs in recv_signals:
            self.inputs[rs] = True
        # Set output
        self.outputs[self.signal_out] = all(self.inputs[signal] for signal in self.signal_in)
            

class Wire(Cell):
    def __init__(self, signal_in):
        super().__init__()
        self.inputs = {signal_in:False}
        self.outputs = {signal_in:False}
        self.signal_in = signal_in
        self.signal_out = signal_in

    def logic(self, recv_signals):
        for rs in recv_signals:
            self.inputs[rs] = True
        self.outputs[self.signal_out] = self.inputs[self.signal_in]
    

class Circuit:
    def __init__(self, c):
        self.iptg = False
        self.start_cells = c
        self.output = False

    # should this pass to all cells? will be added to all media
    def iptg_signal(self, signal):
        self.iptg = signal
        for c in self.start_cells:
            c.update({'iptg':self.iptg})

    # does not work with multiple terminal cells. Fix
    def traverse_circuit(self, cell):
        if not cell.to_cells:
            return cell.outputs
        for to_cell in cell.to_cells:
            return self.traverse_circuit(to_cell)
            
    def get_gfp(self):
        gfp = False
        outputs = {}
        for sc in self.start_cells:
            outputs = self.traverse_circuit(sc)
            if 'gfp' in outputs:
                gfp = outputs['gfp'] or gfp

        return gfp

def main():
    # Run tests

if __name__ == '__main__':
   main()