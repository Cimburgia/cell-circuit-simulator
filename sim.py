#!/usr/bin/env python
import sys

class Cell:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        self.from_cells = []
        self.to_cells = []
    
    def update(self, signals):
        self.logic(signals)
        for tc in self.to_cells:
            tc.update(self.outputs)

    def connect(self, cell):
        self.to_cells.append(cell)
        cell.from_cells.append(self)
        cell.update(self.outputs)
    
class Sender(Cell):
    def __init__(self):
        super(Sender, self).__init__()
        self.inputs = {'ipgt':False}
        self.outputs = {'ahl':False}

    def logic(self, signals):
        for k,v in signals.items():
            if k in self.inputs:
                self.inputs[k] = v
        self.outputs['ahl'] = self.inputs['ipgt']
        self.outputs['ipgt'] = self.inputs['ipgt']

class Receiver(Cell):
    def __init__(self):
        super(Receiver, self).__init__()
        self.inputs = {'ipgt':False,
                       'ahl':False}
        self.outputs = {'gfp':False}
    
    def logic(self, signals):
        for k,v in signals.items():
            if k in self.inputs:
                self.inputs[k] = v
        self.outputs['gfp'] = self.inputs['ipgt'] & self.inputs['ahl']

class Circuit:
    def __init__(self, c):
        self.ipgt = False
        self.start_cells = [c]
        self.output = False

    def ipgt_signal(self, signal):
        self.ipgt = signal
        for c in self.start_cells:
            c.update({'ipgt':self.ipgt})

    def traverse_circuit(self, cell):
        if not cell.to_cells:
            return cell.outputs
        for to_cell in cell.to_cells:
            if self.traverse_circuit(to_cell):
                return True
            
    def get_gfp(self):
        gfp = False
        outputs = {}
        for sc in self.start_cells:
            outputs = self.traverse_circuit(sc)
            if 'gfp' in outputs:
                gfp = outputs['gfp'] or gfp

        return gfp

def main():
    s = Sender()
    r = Receiver()
    s.connect(r)

    c = Circuit(s)
    
    c.ipgt_signal(True)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

    c.ipgt_signal(False)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

if __name__ == '__main__':
   main()