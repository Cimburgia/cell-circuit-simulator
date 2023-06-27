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
        self.inputs = {'iptg':False}
        self.outputs = {'ahl':False}

    def logic(self, signals):
        for k,v in signals.items():
            if k in self.inputs:
                self.inputs[k] = v
        self.outputs['ahl'] = self.inputs['iptg']
        self.outputs['iptg'] = self.inputs['iptg']

class Receiver(Cell):
    def __init__(self):
        super(Receiver, self).__init__()
        self.inputs = {'iptg':False,
                       'ahl':False}
        self.outputs = {'gfp':False}
    
    def logic(self, signals):
        for k,v in signals.items():
            if k in self.inputs:
                self.inputs[k] = v
        self.outputs['gfp'] = self.inputs['iptg'] & self.inputs['ahl']

class Circuit:
    def __init__(self, c):
        self.iptg = False
        self.start_cells = [c]
        self.output = False

    # should this pass to all cells? will be added to all media
    def iptg_signal(self, signal):
        self.iptg = signal
        for c in self.start_cells:
            c.update({'iptg':self.iptg})

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
    # Update here
    # Basic test, eventually replace 
    s = Sender()
    r = Receiver()
    r1 = Receiver()
    s.connect(r)
    s.connect(r1)

    c = Circuit(s)
    
    c.iptg_signal(True)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    print("----------------------------------------------------")

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

    
    print("----------------------------------------------------")

    for sig in r1.outputs.keys():
        print(sig)
        print(r1.outputs[sig])

    print("----------------------------------------------------")

    #r.outputs['gfp'] = False
    print("output: {}".format(c.get_gfp()))
    print("----------------------------------------------------")

    c.iptg_signal(False)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])
    print("----------------------------------------------------")

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])
    print("----------------------------------------------------")

    print("output: {}".format(c.get_gfp()))
    

if __name__ == '__main__':
   main()