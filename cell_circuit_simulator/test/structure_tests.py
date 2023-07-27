import simulator.sim as sim   # The code to test
import pytest

#What you're testing and a decription of what you expect to happen
'''
    Functions to add:
    - Circuit.get_outputs() [need to call build before we get full list]
    - Circuit.build_circuit()
    - Wire to be created when Cell.connect is called
    - Circuit.get_wires(built_circuit) -> list of wires

'''
def test_get_outputs1():
    sender = sim.Sender('iptg', 'ahl')
    circuit = sim.circuit(sender)
    circuit.build_circuit()
    o = circuit.get_outputs()
    assert o == ['ahl']


def test_get_outputs2():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit(sender)
    sender.connect(receiver_cell)
    circuit.build_circuit()
    o = circuit.get_outputs()
    assert o == ['ahl', 'gfp']

def test_get_outputs3():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit(sender)
    sender.connect(receiver_cell)
    o = circuit.get_outputs()
    assert o == ['ahl']


def test_connect_cells1():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit(sender)
    sender.connect(receiver_cell)
    circuit.build_circuit()
    assert circuit.get_wires() == [Wire]

def test_connect_cells2():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell1 = sim.receiver(['ahl', 'iptg'], 'gfp')
    receiver_cell2 = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit(sender)
    sender.connect(receiver_cell1)
    sender.connect(receiver_cell2)
    circuit.build_circuit()
    assert circuit.get_wires() == [Wire, Wire]

# sender->wire->reciever
def test_build_circuit():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit(sender)
    sender.connect(receiver_cell) 
    # traverse connections
    assert circuit.build_circuit() == [[1, 1],
                                       [0, 1]] or circuit.build_circuit() == [[receiver_cell],[]]
    
# sender connects to wire1 and wire 2. Both wire1 and wire2 connect to receiver.
def test_build_circuit2():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell1 = sim.receiver(['ahl', 'iptg'], 'gfp')
    receiver_cell2 = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit(sender)
    sender.connect(receiver_cell1)
    sender.connect(receiver_cell2)
    circuit.build_circuit() 
    # traverse connections
    assert circuit.build_circuit() == [[1, 1, 1],
                                       [0, 1, 0]
                                       [0, 0, 1]] or circuit.build_circuit() == [[receiver_cell1, receiver_cell1],[], []]
    
def test_build_circuit3():
    s = sim.Sender('iptg', 'ahl')
    s1 = sim.Sender('iptg', 'ahl')
    s2 = sim.Sender('iptg', 'ahl')
    r = sim.receiver(['ahl', 'iptg'], 'gfp')
    r1 = sim.receiver(['ahl', 'iptg'], 'gfp')
    r2 = sim.receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.circuit([s, s1, s2])
    s.connect(r)
    s.connect(r1)
    s.connect(r2)

    s1.connect(r)
    s1.connect(r1)
    s1.connect(r2)

    s2.connect(r)
    s2.connect(r1)
    s2.connect(r2)
    circuit.build_circuit() 
    # traverse connections
    assert circuit.build_circuit() == [[1, 0, 0, 1, 1, 1],
                                       [0, 1, 0, 1, 1, 1]
                                       [0, 0, 1, 1, 1, 1]
                                       [0, 0, 0, 1, 0, 0]
                                       [0, 0, 0, 0, 1, 0]
                                       [0, 0, 0, 0, 0, 1]] or circuit.build_circuit() == [[r, r1, r2], [r, r1, r2], [r, r1, r2], [], [], []]
