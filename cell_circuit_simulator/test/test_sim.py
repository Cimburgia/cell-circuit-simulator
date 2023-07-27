from framework.cell import Cell
from framework.sender import Sender
from framework.receiver import Receiver
from framework.wire import Wire
from framework.circuit import Circuit
import pytest

def create_Circuit_oneS_oneW_oneR():
    s = Sender('iptg', 'ahl')
    w = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')

    c = Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()
    return [s, w, r, c]

def create_Circuit_oneS_twoW_twoR():
    s = Sender('iptg', 'ahl')
    w = Wire('ahl')
    w1 = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')
    r1 = Receiver(['ahl', 'iptg'], 'gfp')

    c = Circuit(s)

    s.connect(w)
    w.connect(r)
    s.connect(w1)
    w.connect(r1)
    c.add_iptg()
    return [s, w, w1, r, r1, c]

def create_Circuit_twoS_twoW_oneR():
    sender1 = Sender('iptg', 'ahl')
    sender2 = Sender('iptg', 'ahl')
    receiver = Receiver(['iptg', 'ahl'], 'gfp')
    Wire1 = Wire('ahl')
    Wire2 = Wire('ahl')
    sender1.connect(Wire1)
    Wire1.connect(receiver)
    sender2.connect(Wire2)
    Wire2.connect(receiver)
    circuit = Circuit([sender1, sender2])
    circuit.add_iptg()
    return circuit

    

def create_Circuit_threeS_NineW_threeR():
    s = Sender('iptg', 'ahl')
    s1 = Sender('iptg', 'ahl')
    s2 = Sender('iptg', 'ahl')
    w = Wire('ahl')
    w1 = Wire('ahl')
    w2 = Wire('ahl')
    w3 = Wire('ahl')
    w4 = Wire('ahl')
    w5 = Wire('ahl')
    w6 = Wire('ahl')
    w7 = Wire('ahl')
    w8 = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')
    r1 = Receiver(['ahl', 'iptg'], 'gfp')
    r2 = Receiver(['ahl', 'iptg'], 'gfp')


    c = Circuit([s, s1, s2])

    s.connect(w)
    w.connect(r)
    s.connect(w1)
    w1.connect(r1)
    s.connect(w2)
    w2.connect(r2)

    s1.connect(w3)
    w3.connect(r)
    s1.connect(w4)
    w4.connect(r1)
    s1.connect(w5)
    w5.connect(r2)

    s2.connect(w6)
    w6.connect(r)
    s2.connect(w7)
    w7.connect(r1)
    s2.connect(w8)
    w8.connect(r2)

    return [s, s1, s2, w, w1, w2, w3, w4, w5, w6, w7, w8, r, r1, r2, c]

def create_Circuit_oneS_oneW_threeR():
    s = Sender('iptg', 'ahl')
    w = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')
    r1 = Receiver(['ahl', 'iptg'], 'gfp')
    r2 = Receiver(['ahl', 'iptg'], 'gfp')

    c = Circuit(s)

    s.connect(w)
    w.connect(r)
    w.connect(r1)
    w.connect(r2)

    c.add_iptg()
    return[s, w, r, r1, r2, c]

def create_Circuit_threeS_oneW_oneR():
    s = Sender('iptg', 'ahl')
    s1 = Sender('iptg', 'ahl')
    s2= Sender('iptg', 'ahl')
    w = Wire('ahl')
    r = Receiver(['ahl', 'iptg'], 'gfp')
    

    c = Circuit(s)

    s.connect(w)
    s1.connect(w)
    s2.connect(w)
    w.connect(r)
    
    
    c.add_iptg()
    return[s, s1, s2, w, r, c]

#Simple unit test
def test_Wire_simple1():
    wire = Wire('iptg')
    wire.update(['iptg'])
    assert wire.inputs['iptg'] and wire.outputs['iptg'] == True

#Simple unit test
def test_Wire_simple2():
    wire = Wire('ahl')
    wire.logic(['ahl'])
    assert wire.inputs['ahl'] and wire.inputs['ahl'] == True

#Simple unit test
def test_sender_simple1():
    sender = Sender('iptg', 'ahl')
    sender.update(['iptg'])
    assert sender.inputs['iptg'] and sender.outputs['ahl'] == True

#Simple unit test
def test_sender_simple2():
    sender = Sender('iptg', 'ahl')
    sender.logic(['iptg'])
    assert sender.inputs['iptg'] and sender.outputs['ahl'] == True

#Simple unit test
def test_Receiver_simple1():
    receiver = Receiver(['ahl', 'iptg'], 'gfp')
    receiver.update(['ahl', 'iptg'])
    assert receiver.inputs['ahl'] and receiver.inputs['iptg'] and receiver.outputs['gfp'] == True

#Simple unit test
def test_Receiver_simple2():
    receiver = Receiver(['ahl', 'iptg'], 'gfp')
    receiver.logic(['ahl', 'iptg'])
    assert receiver.inputs['ahl'] and receiver.inputs['iptg'] and receiver.outputs['gfp'] == True
    

#Integration test
def test_cell_connection_SR():
    send_cell = Sender('iptg', 'ahl')
    receiver_cell = Receiver(['ahl', 'iptg'], 'gfp')
    send_cell.connect(receiver_cell)
    assert receiver_cell in send_cell.to_cells and send_cell in receiver_cell.from_cells

#Integration test
def test_cell_connection_SW():
    send_cell = Sender('iptg', 'ahl')
    wire = Wire('iptg')
    send_cell.connect(wire)
    assert wire in send_cell.to_cells and send_cell in wire.from_cells

#Integration test
def test_cell_connection_WR():
    wire = Wire('iptg')
    receiver_cell = Receiver(['ahl', 'iptg'], 'gfp')
    wire.connect(receiver_cell)
    assert receiver_cell in wire.to_cells and wire in receiver_cell.from_cells

#Integration test
def test_cell_connection_WS():
    wire = Wire('iptg')
    send_cell = Sender('iptg', 'ahl')
    wire.connect(send_cell)
    assert send_cell in wire.to_cells and wire in send_cell.from_cells

#Integration test
def test_cell_connection_RW():
    receiver_cell = Receiver(['ahl', 'iptg'], 'gfp')
    wire = Wire('iptg')
    receiver_cell.connect(wire)
    assert wire in receiver_cell.to_cells and receiver_cell in wire.from_cells


#Functional Test
def test_Circuit_simulation1():
    sender = Sender('iptg', 'ahl')
    receiver = Receiver(['ahl', 'iptg'], 'gfp')
    sender.connect(receiver)
    circuit = Circuit(sender)
    circuit.add_iptg()
    assert circuit.simulate(['iptg']) == True

#Functional Test
def test_Circuit_simulation2():
    sender = Sender('iptg', 'ahl')
    wire = Wire('iptg')
    sender.connect(wire)
    circuit = Circuit(sender)
    circuit.add_iptg()
    assert circuit.simulate(['iptg']) == True

#End to end testing
def test_end_to_end_simulation1():
    circuit = create_Circuit_oneS_oneW_oneR()[3]
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation2():
    circuit = create_Circuit_oneS_twoW_twoR()[5]
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation3():
    circuit = create_Circuit_twoS_twoW_oneR()
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation4():
    circuit = create_Circuit_threeS_NineW_threeR()[15]
    circuit.add_iptg()
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation5():
    circuit = create_Circuit_oneS_oneW_threeR()[5]
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation6():
    circuit = create_Circuit_threeS_oneW_oneR()[5]    
    assert circuit.simulate(['iptg', 'ahl']) == True


#End to end testing
#Test simple Circuit with one sender, one Wire, and one Receiver
def test_Circuit_one1():
    returns = create_Circuit_oneS_oneW_oneR()
    c = returns[3]
    r = returns[2]
    assert r.outputs['gfp'] == False
    
#End to end testing
def test_Circuit_one2():
    returns = create_Circuit_oneS_oneW_oneR()
    c = returns[3]
    r = returns[2]
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

#End to end testing
#Test Circuit with one sender, two Wires, and two Receiver
def test_Circuit_two1():
    returns = create_Circuit_oneS_twoW_twoR()
    c = returns[5]
    r = returns[3]
    r1 = returns[4]
    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False

#End to end testing
def test_Circuit_two2():
    returns = create_Circuit_oneS_twoW_twoR()
    c = returns[5]
    r = returns[3]
    r1 = returns[4]
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] == True

#End to end testing
#Test Circuit with 3 senders, 9 Wires, and three Receivers
def test_Circuit_three1():
    returns = create_Circuit_threeS_NineW_threeR()
    c = returns[15]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c.add_iptg()
    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
   

#End to end testing
def test_Circuit_three2():
    returns = create_Circuit_threeS_NineW_threeR()
    c = returns[15]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c.add_iptg()
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True

#End to end testing
#Test readOutput with one sender, one Wire, and one Receiver
def test_read_output_one1():
    returns = create_Circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    assert c.read_output(s) == False and c.read_output(w) == False and c.read_output(r) == False

#End to end testing
def test_read_output_one2():
    returns = create_Circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    c.simulate('iptg')
    assert c.read_output(s) and c.read_output(w) and c.read_output(r) == True


#End to end testing
#Test readOutput with one sender, two Wires, and two Receivers
#This test failed because c.read_output(s) is True instead of false before c.simulate('iptg') is ran. 
def test_read_output_two1():
    returns = create_Circuit_oneS_twoW_twoR()
    s = returns[0]
    w = returns[1]
    w1 = returns[2]
    r = returns[3]
    r1 = returns[4]
    c = returns[5]

    assert c.read_output(s) == False and c.read_output(w) == False and c.read_output(w1) == False and c.read_output(r) == False and c.read_output(r1) == False
    c.simulate('iptg')

#End to end testing
def test_read_output_two2():
    returns = create_Circuit_oneS_twoW_twoR()
    s = returns[0]
    w = returns[1]
    w1 = returns[2]
    r = returns[3]
    r1 = returns[4]
    c = returns[5]

    c.simulate('iptg')
    assert c.read_output(s) and c.read_output(w) and c.read_output(w1) and c.read_output(r) and c.read_output(r1) == True

#End to end testing
def test_Wire():
    returns = create_Circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    c.simulate('iptg')
    assert w.inputs['ahl'] and w.outputs['ahl'] == True

#End to end testing
#-Where there is no c.add_iptg(), w.inputs['iptg'] gives error, but s.inputs['iptg'] and r.inputs['iptg'] return false
def test_add_iptg1():
    returns = create_Circuit_threeS_NineW_threeR()
    s = returns[0]
    s1 = returns[1]
    s2 = returns[2]
    w = returns[3]
    w1 = returns[4]
    w2 = returns[5]
    w3 = returns[6]
    w4 = returns[7]
    w5 = returns[8]
    w6 = returns[9]
    w7 = returns[10]
    w8 = returns[11]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c = returns[15]
    assert s.inputs['iptg'] == False and s1.inputs['iptg'] == False and s2.inputs['iptg'] == False and r.inputs['iptg'] == False and r1.inputs['iptg'] == False  and r2.inputs['iptg'] == False

#End to end testing
def test_add_iptg2():
    returns = create_Circuit_threeS_NineW_threeR()
    s = returns[0]
    s1 = returns[1]
    s2 = returns[2]
    w = returns[3]
    w1 = returns[4]
    w2 = returns[5]
    w3 = returns[6]
    w4 = returns[7]
    w5 = returns[8]
    w6 = returns[9]
    w7 = returns[10]
    w8 = returns[11]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c = returns[15]
    c.add_iptg()
    assert s.inputs['iptg'] and s1.inputs['iptg'] and s2.inputs['iptg'] and r.inputs['iptg'] and r1.inputs['iptg'] and r2.inputs['iptg'] == True

#End to end testing
#Test simple Circuit with one sender, and one Wire that connects to 3 recievers
def test_Circuit_one_Wire_to_many_recievers1():
    returns = create_Circuit_oneS_oneW_threeR()
    r = returns[2]
    r1 = returns[3]
    r2 = returns[4]
    c = returns[5]

    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
    c.simulate('iptg')

#End to end testing
def test_Circuit_one_Wire_to_many_recievers2():
    returns = create_Circuit_oneS_oneW_threeR()
    r = returns[2]
    r1 = returns[3]
    r2 = returns[4]
    c = returns[5]

    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True

#End to end testing
#Test simple Circuit with one sender, and one Wire that connects to 3 recievers
def test_Circuit_many_senders_to_one_Wire1():
    returns = create_Circuit_threeS_oneW_oneR()
    r = returns[4]
    c = returns[5]
    assert r.outputs['gfp'] == False
    c.simulate('iptg')

#End to end testing
def test_Circuit_many_senders_to_one_Wire2():
    returns = create_Circuit_threeS_oneW_oneR()
    r = returns[4]
    c = returns[5]
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

#Edge Case Test
def test_Circuit_with_no_input():
    sender = Sender('iptg', 'ahl')
    circuit = Circuit([sender])
    # The Circuit with no input
    assert circuit.simulate([]) == False

#Edge Case Test
def test_Circuit_with_wrong_input():
    sender = Sender('iptg', 'ahl')
    circuit = Circuit([sender])
    # The Circuit with no input
    assert circuit.simulate(['gfp']) == False

#Edge Case Test
def test_cell_connection_SS():
    send_cell1 = Sender('iptg', 'ahl')
    send_cell2 = Sender('iptg', 'ahl')
    send_cell1.connect(send_cell2)
    assert send_cell2 in send_cell1.to_cells and send_cell1 in send_cell2.from_cells

#Edge Case Test
def test_cell_connection_WW():
    Wire1 = Wire('iptg')
    Wire2 = Wire('iptg')
    Wire1.connect(Wire2)
    assert Wire2 in Wire1.to_cells and Wire1 in Wire2.from_cells

#Edge Case Test
def test_cell_connection_RR():
    Receiver_cell1 = Receiver(['ahl', 'iptg'], 'gfp')
    Receiver_cell2 = Receiver(['ahl', 'iptg'], 'gfp')
    Receiver_cell1.connect(Receiver_cell2)
    assert Receiver_cell2 in Receiver_cell1.to_cells and Receiver_cell1 in Receiver_cell2.from_cells

#Edge Case Test
def test_Wire_edge1():
    wire = Wire('iptg')
    wire.update(['ahl'])
    assert wire.inputs['iptg'] == False and wire.outputs['iptg'] == False

#Edge Case Test
def test_Wire_edge2():
    wire = Wire('ahl')
    wire.logic(['iptg'])
    assert wire.inputs['ahl'] == False and wire.inputs['ahl'] == False

#Edge Case Test
def test_sender_edge1():
    sender = Sender('iptg', 'ahl')
    sender.update(['ahl'])
    assert sender.inputs['iptg'] == False and sender.outputs['ahl'] == False

#Edge Case Test
def test_sender_edge2():
    sender = Sender('iptg', 'ahl')
    sender.logic(['ahl'])
    assert sender.inputs['iptg'] == False and sender.outputs['ahl'] == False

#Edge Case Test
def test_Receiver_edge1():
    receiver = Receiver(['ahl', 'iptg'], 'gfp')
    receiver.update(['gfp'])
    assert receiver.inputs['ahl'] == False and receiver.inputs['iptg'] == False and receiver.outputs['gfp'] == False

#Edge Case Test
def test_Receiver_edge2():
    receiver = Receiver(['ahl', 'iptg'], 'gfp')
    receiver.logic(['gfp'])
    assert receiver.inputs['ahl'] == False and receiver.inputs['iptg'] == False and receiver.outputs['gfp'] == False

