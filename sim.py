#!/usr/bin/env python
import sys
from cell import Cell
from sender import Sender
from receiver import Receiver
from wire import Wire
from circuit import Circuit

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