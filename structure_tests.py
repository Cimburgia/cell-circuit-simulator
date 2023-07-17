import sim   # The code to test
import pytest

'''
    Functions to add:
    - Circuit.get_outputs() [need to call build before we get full list]
    - Circuit.build_circuit()
    - Wire to be created when Cell.connect is called
    - Circuit.get_wires(built_circuit) -> list of wires
'''
def test_get_outputs1():
    sender = sim.Sender('iptg', 'ahl')
    circuit = sim.Circuit(sender)
    circuit.build_circuit()
    o = circuit.get_outputs()
    assert o == ['ahl']

def test_get_outputs2():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.Circuit(sender)
    sender.connect(receiver_cell)
    circuit.build_circuit()
    o = circuit.get_outputs()
    assert o == ['ahl', 'gfp']


def test_connect_cells1():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.Circuit(sender)
    sender.connect(receiver_cell)
    circuit.build_circuit()
    assert circuit.get_wires() == [Wire]

def test_connect_cells2():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell1 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    receiver_cell2 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.Circuit(sender)
    sender.connect(receiver_cell1)
    sender.connect(receiver_cell2)
    circuit.build_circuit()
    assert circuit.get_wires() == [Wire, Wire]

# sender->wire->reciever
def test_build_circuit():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.Circuit(sender)
    sender.connect(receiver_cell) 
    # traverse connections
    assert circuit.build_circuit() == [[1, 1, 0],
                                       [0, 1, 1],
                                       [0, 0, 1]] or circuit.build_circuit() == [[wire],[receiver_cell],[]]
    
# sender connects to wire1 and wire 2. Both wire1 and wire2 connect to receiver.
def test_build_circuit2():
    sender = sim.Sender('iptg', 'ahl')
    receiver_cell1 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    receiver_cell2 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    circuit = sim.Circuit(sender)
    sender.connect(receiver_cell1)
    sender.connect(receiver_cell2)
    circuit.build_circuit() 
    # traverse connections
    circuit.build_circuit() == [[wire1, wire2],[receiver_cell1],[], [receiver_cell2], []]
    
