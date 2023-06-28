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
        self.start_cells = c
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
    # Update here!
    # Basic test, eventually replace 
    # A test with one sender and two receivers
    '''
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
    
    '''

    '''
    #A test with 2 senders and 3 recievers
    s = Sender()
    s1 = Sender()
    r = Receiver()
    r1 = Receiver()
    r2 = Receiver()
    s.connect(r)
    s1.connect(r1)
    s1.connect(r2)

    c = Circuit([s, s1])
    
    c.iptg_signal(True)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    print("----------------------------------------------------")

    for sig in s1.outputs.keys():
        print(sig)
        print(s1.outputs[sig])

    print("----------------------------------------------------")

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

    
    print("----------------------------------------------------")

    for sig in r1.outputs.keys():
        print(sig)
        print(r1.outputs[sig])

    print("----------------------------------------------------")

    for sig in r2.outputs.keys():
        print(sig)
        print(r2.outputs[sig])

    print("----------------------------------------------------")

    #r.outputs['gfp'] = False
    print("output: {}".format(c.get_gfp()))
    print("----------------------------------------------------")

    c.iptg_signal(False)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    print("----------------------------------------------------")

    for sig in s1.outputs.keys():
        print(sig)
        print(s1.outputs[sig])

    print("----------------------------------------------------")

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

    
    print("----------------------------------------------------")

    for sig in r1.outputs.keys():
        print(sig)
        print(r1.outputs[sig])

    print("----------------------------------------------------")

    for sig in r2.outputs.keys():
        print(sig)
        print(r2.outputs[sig])

    print("----------------------------------------------------")

    print("output: {}".format(c.get_gfp()))
    '''


    #A test with 5 senders and 9 recievers
    s = Sender()
    s1 = Sender()
    s2 = Sender()
    s3 = Sender()
    s4 = Sender()
    r = Receiver()
    r1 = Receiver()
    r2 = Receiver()
    r3 = Receiver()
    r4 = Receiver()
    r5 = Receiver()
    r6 = Receiver()
    r7 = Receiver()
    r8 = Receiver()
    s.connect(r)
    s.connect(r1)
    s.connect(r2)
    s.connect(r3)
    s.connect(r4)
    s.connect(r5)
    s.connect(r6)
    s.connect(r7)
    s.connect(r8)

    s1.connect(r)
    s1.connect(r1)
    s1.connect(r2)
    s1.connect(r3)
    s1.connect(r4)
    s1.connect(r5)
    s1.connect(r6)
    s1.connect(r7)
    s1.connect(r8)

    s2.connect(r6)
    s2.connect(r7)
    s2.connect(r8)

    s3.connect(r2)
    s3.connect(r3)

    s4.connect(r1)
    s4.connect(r2)
    s4.connect(r6)
    s4.connect(r7)
    s4.connect(r8)


    c = Circuit([s, s1, s2, s3, s4])
    
    c.iptg_signal(True)
    
    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    print("----------------------------------------------------")

    for sig in s1.outputs.keys():
        print(sig)
        print(s1.outputs[sig])

    print("----------------------------------------------------")

    for sig in s2.outputs.keys():
        print(sig)
        print(s2.outputs[sig])

    print("----------------------------------------------------")

    for sig in s3.outputs.keys():
        print(sig)
        print(s3.outputs[sig])

    print("----------------------------------------------------")

    for sig in s4.outputs.keys():
        print(sig)
        print(s4.outputs[sig])

    print("----------------------------------------------------")

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

    
    print("----------------------------------------------------")

    for sig in r1.outputs.keys():
        print(sig)
        print(r1.outputs[sig])

    print("----------------------------------------------------")

    for sig in r2.outputs.keys():
        print(sig)
        print(r2.outputs[sig])

    print("----------------------------------------------------")

    for sig in r3.outputs.keys():
        print(sig)
        print(r3.outputs[sig])

    print("----------------------------------------------------")

    for sig in r4.outputs.keys():
        print(sig)
        print(r4.outputs[sig])

    print("----------------------------------------------------")

    for sig in r5.outputs.keys():
        print(sig)
        print(r5.outputs[sig])

    print("----------------------------------------------------")

    for sig in r6.outputs.keys():
        print(sig)
        print(r6.outputs[sig])

    print("----------------------------------------------------")

    for sig in r7.outputs.keys():
        print(sig)
        print(r7.outputs[sig])

    print("----------------------------------------------------")

    for sig in r8.outputs.keys():
        print(sig)
        print(r8.outputs[sig])

    print("----------------------------------------------------")

    #r.outputs['gfp'] = False
    print("output: {}".format(c.get_gfp()))
    print("----------------------------------------------------")

    c.iptg_signal(False)

    for sig in s.outputs.keys():
        print(sig)
        print(s.outputs[sig])

    print("----------------------------------------------------")

    for sig in s1.outputs.keys():
        print(sig)
        print(s1.outputs[sig])

    print("----------------------------------------------------")

    for sig in s2.outputs.keys():
        print(sig)
        print(s2.outputs[sig])

    print("----------------------------------------------------")

    for sig in s3.outputs.keys():
        print(sig)
        print(s3.outputs[sig])

    print("----------------------------------------------------")

    for sig in s4.outputs.keys():
        print(sig)
        print(s4.outputs[sig])

    print("----------------------------------------------------")

    for sig in r.outputs.keys():
        print(sig)
        print(r.outputs[sig])

    
    print("----------------------------------------------------")

    for sig in r1.outputs.keys():
        print(sig)
        print(r1.outputs[sig])

    print("----------------------------------------------------")

    for sig in r2.outputs.keys():
        print(sig)
        print(r2.outputs[sig])

    print("----------------------------------------------------")

    for sig in r3.outputs.keys():
        print(sig)
        print(r3.outputs[sig])

    print("----------------------------------------------------")

    for sig in r4.outputs.keys():
        print(sig)
        print(r4.outputs[sig])

    print("----------------------------------------------------")

    for sig in r5.outputs.keys():
        print(sig)
        print(r5.outputs[sig])

    print("----------------------------------------------------")

    for sig in r6.outputs.keys():
        print(sig)
        print(r6.outputs[sig])

    print("----------------------------------------------------")

    for sig in r7.outputs.keys():
        print(sig)
        print(r7.outputs[sig])

    print("----------------------------------------------------")

    for sig in r8.outputs.keys():
        print(sig)
        print(r8.outputs[sig])

    print("----------------------------------------------------")

    #r.outputs['gfp'] = False
    print("output: {}".format(c.get_gfp()))
    print("----------------------------------------------------")


if __name__ == '__main__':
   main()