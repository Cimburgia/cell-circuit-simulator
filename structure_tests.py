import sim   # The code to test
import pytest

'''
    Functions to add:
    - Circuit.get_outputs() [need to call build before we get full list]
    - Circuit.build_circuit()
    - Wire to be created when Cell.connect is called
    - Circuit.get_wires(built_circuit) -> list of wires
'''
def test_get_outputs():
    # instantiate a sender with 'iptg', 'ahl'
    # instantiate a receiver 'iptg', 'ahl', 'gfp'
    # instantiate a circuit
    # connect r and c
    # call o = circuit.get_outputs()
    assert o == ['ahl', 'gfp']

def test_connect_cells():
    # s = sender
    # r = receiver
    # s.connect(r)
    # c = circuit(s)

    assert c.get_wires() == [Wire]

def test_build_circuit():
    # instantiate cells
    # define cell connections
    # Add cells to circuit
    # taverse connections
    # return adjacency list or matrix
    # ex.
    # A->B->C 
    # List: [[B],[C],[]]
    # Matrix: [[1, 1, 0],
    #          [0, 1, 1],
    #          [0, 0, 1]]