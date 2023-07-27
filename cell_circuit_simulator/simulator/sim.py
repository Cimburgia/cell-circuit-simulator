import numpy as np
from framework.cell import Cell
from framework.sender import Sender
from framework.receiver import Receiver
from framework.wire import Wire
from framework.circuit import Circuit

"""
This will eventually be what does the simulation and compilation of the circuits. This
code will call on model.py to help in making decisions about how the circuit should be
placed and what gates to use. We will also have this contain information specified at
run time by the user such as:
- Code to compile
- Expected outputs
- Hydrogel properties

Eventually, it will make sense to have a library of cell types
"""
def main():
    # Run tests
    
    s = Sender('iptg', 'ahl')
    w = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')

    c = Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()
    c.simulate('iptg')
    print(c.read_output(s))
    print(c.read_output(w))
    print(c.read_output(r))

if __name__ == '__main__':
   main()