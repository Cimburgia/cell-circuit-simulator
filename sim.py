#!/usr/bin/env python
import sys

class Cell:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        self.from_cells = []
        self.to_cells = []

    
    def update(self, signals_in):
        """
        Calls the logic operation on itself, which processes the 
        current inputs into outputs. Then looks at all its neighboring cells
        and calls update on them.
        """
        self.logic(signals_in)
        for tc in self.to_cells:
            tc.update(self.outputs)

    def connect(self, cell):
        """
        Connects itself to another cell
        """
        self.to_cells.append(cell)
        cell.from_cells.append(self)
    
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
    
    #Sets outputs to True when both inputs IPTG and AHL are True
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

    #Forwards AHL signal
    def logic(self, recv_signals):
        for rs in recv_signals:
            self.inputs[rs] = True
        self.outputs[self.signal_out] = self.inputs[self.signal_in]

# Class where cells are represented as a graph
class Circuit:
    def __init__(self, start_cells):
        if not isinstance(start_cells, list):
            start_cells = [start_cells]
        self.signals = []
        self.cells = start_cells

    # Adds iptg to all cells
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

    # Read output of cell
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
   # w1 = Wire('ahl')
    #r = Receiver(['ahl', 'iptg'], 'gfp')
    #r1 = Receiver(['ahl', 'iptg'], 'gfp')

    c = Circuit([s])

    print(c.read_output(s))
    print(c.read_output(w))
   # print(c.read_output(w1))
   # print(c.read_output(r))
   # print(c.read_output(r1))
    print("--------------------------")

    s.connect(w)
    #w.connect(r)
    #s.connect(w1)
    #w.connect(r1)

    print(c.read_output(s))
    print(c.read_output(w))
    #print(c.read_output(w1))
    #print(c.read_output(r))
    #print(c.read_output(r1))
    print("--------------------------")


    c.add_iptg()

    print(c.read_output(s))
    print(c.read_output(w))
    #print(c.read_output(w1))
    #print(c.read_output(r))
    #print(c.read_output(r1))
    print("--------------------------")
    c.simulate('iptg')
    print(c.read_output(s))
    print(c.read_output(w))
    #print(c.read_output(w1))
    #print(c.read_output(r))
    #print(c.read_output(r1))


if __name__ == '__main__':
   main()