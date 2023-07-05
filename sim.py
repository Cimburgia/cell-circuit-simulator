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

# Class where cells are represented as a graph
class Circuit:
    def __init__(self, start_cells):
        self.signals = []
        self.cells = [start_cells]

    # Add iptg
    def add_iptg(self, node = None, visited = None):
        if visited is None:
            visited = set()
        if node is None:
            for c in self.cells:
                self.add_iptg(c, visited)
        else:
            visited.add(node)
            node.inputs['iptg'] = True
            for tc in node.to_cells:
                if tc not in visited:
                    self.add_iptg(tc, visited)

    # Read output of circuit
    def read_output(self, cell):
        if not cell.to_cells:
            return cell.outputs[cell.signal_out]
        
        for tc in cell.to_cells:
            if self.read_output(tc):
                return True
        
        return False
        
    # Run circuit
    def simulate(self, signal):
        out = False
        for c in self.cells:
            c.update(signal)
            out = out | self.read_output(c)
        return out

def main():
    # Run tests
    s = Sender('iptg', 'ahl')
    w = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')

    c = Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()

    print(s.inputs['iptg'])
    print(r.inputs['iptg'])
    print(r.outputs['gfp'])
    print(c.simulate('iptg'))
    print(r.outputs['gfp'])

if __name__ == '__main__':
   main()