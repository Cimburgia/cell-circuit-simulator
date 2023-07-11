import sim   # The code to test
import pytest

def create_circuit_oneS_oneW_oneR():
    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()
    return [s, w, r, c]

def create_circuit_oneS_twoW_twoR():
    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    w1 = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')
    r1 = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)
    s.connect(w1)
    w.connect(r1)
    c.add_iptg()
    return [s, w, w1, r, r1, c]

def create_circuit_twoS_twoW_oneR():
    sender1 = sim.Sender('iptg', 'ahl')
    sender2 = sim.Sender('iptg', 'ahl')
    receiver = sim.Receiver(['iptg', 'ahl'], 'gfp')
    wire1 = sim.Wire('ahl')
    wire2 = sim.Wire('ahl')
    sender1.connect(wire1)
    wire1.connect(receiver)
    sender2.connect(wire2)
    wire2.connect(receiver)
    circuit = sim.Circuit([sender1, sender2])
    circuit.add_iptg()
    return circuit

    

def create_circuit_threeS_NineW_threeR():
    s = sim.Sender('iptg', 'ahl')
    s1 = sim.Sender('iptg', 'ahl')
    s2 = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    w1 = sim.Wire('ahl')
    w2 = sim.Wire('ahl')
    w3 = sim.Wire('ahl')
    w4 = sim.Wire('ahl')
    w5 = sim.Wire('ahl')
    w6 = sim.Wire('ahl')
    w7 = sim.Wire('ahl')
    w8 = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')
    r1 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    r2 = sim.Receiver(['ahl', 'iptg'], 'gfp')


    c = sim.Circuit([s, s1, s2])

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

def create_circuit_oneS_oneW_threeR():
    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')
    r1 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    r2 = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)
    w.connect(r1)
    w.connect(r2)

    c.add_iptg()
    return[s, w, r, r1, r2, c]

def create_circuit_threeS_oneW_oneR():
    s = sim.Sender('iptg', 'ahl')
    s1 = sim.Sender('iptg', 'ahl')
    s2= sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')
    

    c = sim.Circuit(s)

    s.connect(w)
    s1.connect(w)
    s2.connect(w)
    w.connect(r)
    
    
    c.add_iptg()
    return[s, s1, s2, w, r, c]

#Simple unit test
def test_wire_simple1():
    wire = sim.Wire('iptg')
    wire.update(['iptg'])
    assert wire.inputs['iptg'] and wire.outputs['iptg'] == True

#Simple unit test
def test_wire_simple2():
    wire = sim.Wire('ahl')
    wire.logic(['ahl'])
    assert wire.inputs['ahl'] and wire.inputs['ahl'] == True

#Simple unit test
def test_sender_simple1():
    sender = sim.Sender('iptg', 'ahl')
    sender.update(['iptg'])
    assert sender.inputs['iptg'] and sender.outputs['ahl'] == True

#Simple unit test
def test_sender_simple2():
    sender = sim.Sender('iptg', 'ahl')
    sender.logic(['iptg'])
    assert sender.inputs['iptg'] and sender.outputs['ahl'] == True

#Simple unit test
def test_receiver_simple1():
    receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    receiver.update(['ahl', 'iptg'])
    assert receiver.inputs['ahl'] and receiver.inputs['iptg'] and receiver.outputs['gfp'] == True

#Simple unit test
def test_receiver_simple2():
    receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    receiver.logic(['ahl', 'iptg'])
    assert receiver.inputs['ahl'] and receiver.inputs['iptg'] and receiver.outputs['gfp'] == True
    

#Integration test
def test_cell_connection_SR():
    send_cell = sim.Sender('iptg', 'ahl')
    receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    send_cell.connect(receiver_cell)
    assert receiver_cell in send_cell.to_cells and send_cell in receiver_cell.from_cells

#Integration test
def test_cell_connection_SW():
    send_cell = sim.Sender('iptg', 'ahl')
    wire = sim.Wire('iptg')
    send_cell.connect(wire)
    assert wire in send_cell.to_cells and send_cell in wire.from_cells

#Integration test
def test_cell_connection_WR():
    wire = sim.Wire('iptg')
    receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    wire.connect( receiver_cell)
    assert receiver_cell in wire.to_cells and wire in receiver_cell.from_cells

#Integration test
def test_cell_connection_WS():
    wire = sim.Wire('iptg')
    send_cell = sim.Sender('iptg', 'ahl')
    wire.connect(send_cell)
    assert send_cell in wire.to_cells and wire in send_cell.from_cells

#Integration test
def test_cell_connection_RW():
    receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    wire = sim.Wire('iptg')
    receiver_cell.connect(wire)
    assert wire in receiver_cell.to_cells and receiver_cell in wire.from_cells


#Functional Test
def test_circuit_simulation1():
    sender = sim.Sender('iptg', 'ahl')
    receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    sender.connect(receiver)
    circuit = sim.Circuit(sender)
    circuit.add_iptg()
    assert circuit.simulate(['iptg']) == True

#Functional Test
def test_circuit_simulation2():
    sender = sim.Sender('iptg', 'ahl')
    wire = sim.Wire('iptg')
    sender.connect(wire)
    circuit = sim.Circuit(sender)
    circuit.add_iptg()
    assert circuit.simulate(['iptg']) == True

#End to end testing
def test_end_to_end_simulation1():
    circuit = create_circuit_oneS_oneW_oneR()[3]
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation2():
    circuit = create_circuit_oneS_twoW_twoR()[5]
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation3():
    circuit = create_circuit_twoS_twoW_oneR()
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation4():
    circuit = create_circuit_threeS_NineW_threeR()[15]
    circuit.add_iptg()
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation5():
    circuit = create_circuit_oneS_oneW_threeR()[5]
    assert circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation6():
    circuit = create_circuit_threeS_oneW_oneR()[5]    
    assert circuit.simulate(['iptg', 'ahl']) == True


#End to end testing
#Test simple circuit with one sender, one wire, and one receiver
def test_circuit_one1():
    returns = create_circuit_oneS_oneW_oneR()
    c = returns[3]
    r = returns[2]
    assert r.outputs['gfp'] == False
    
#End to end testing
def test_circuit_one2():
    returns = create_circuit_oneS_oneW_oneR()
    c = returns[3]
    r = returns[2]
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

#End to end testing
#Test circuit with one sender, two wires, and two receiver
def test_circuit_two1():
    returns = create_circuit_oneS_twoW_twoR()
    c = returns[5]
    r = returns[3]
    r1 = returns[4]
    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False

#End to end testing
def test_circuit_two2():
    returns = create_circuit_oneS_twoW_twoR()
    c = returns[5]
    r = returns[3]
    r1 = returns[4]
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] == True

#End to end testing
#Test circuit with 3 senders, 9 wires, and three receivers
def test_circuit_three1():
    returns = create_circuit_threeS_NineW_threeR()
    c = returns[15]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c.add_iptg()
    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
   

#End to end testing
def test_circuit_three2():
    returns = create_circuit_threeS_NineW_threeR()
    c = returns[15]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c.add_iptg()
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True

#End to end testing
#Test readOutput with one sender, one wire, and one receiver
def test_read_output_one1():
    returns = create_circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    assert c.read_output(s) == False and c.read_output(w) == False and c.read_output(r) == False

#End to end testing
def test_read_output_one2():
    returns = create_circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    c.simulate('iptg')
    assert c.read_output(s) and c.read_output(w) and c.read_output(r) == True


#End to end testing
#Test readOutput with one sender, two wires, and two receivers
#This test failed because c.read_output(s) is True instead of false before c.simulate('iptg') is ran. 
def test_read_output_two1():
    returns = create_circuit_oneS_twoW_twoR()
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
    returns = create_circuit_oneS_twoW_twoR()
    s = returns[0]
    w = returns[1]
    w1 = returns[2]
    r = returns[3]
    r1 = returns[4]
    c = returns[5]

    c.simulate('iptg')
    assert c.read_output(s) and c.read_output(w) and c.read_output(w1) and c.read_output(r) and c.read_output(r1) == True

#End to end testing
def test_wire():
    returns = create_circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    c.simulate('iptg')
    assert w.inputs['ahl'] and w.outputs['ahl'] == True

#End to end testing
#-Where there is no c.add_iptg(), w.inputs['iptg'] gives error, but s.inputs['iptg'] and r.inputs['iptg'] return false
def test_add_iptg1():
    returns = create_circuit_threeS_NineW_threeR()
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
    returns = create_circuit_threeS_NineW_threeR()
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
#Test simple circuit with one sender, and one wire that connects to 3 recievers
def test_circuit_one_wire_to_many_recievers1():
    returns = create_circuit_oneS_oneW_threeR()
    r = returns[2]
    r1 = returns[3]
    r2 = returns[4]
    c = returns[5]

    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
    c.simulate('iptg')

#End to end testing
def test_circuit_one_wire_to_many_recievers2():
    returns = create_circuit_oneS_oneW_threeR()
    r = returns[2]
    r1 = returns[3]
    r2 = returns[4]
    c = returns[5]

    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True

#End to end testing
#Test simple circuit with one sender, and one wire that connects to 3 recievers
def test_circuit_many_senders_to_one_wire1():
    returns = create_circuit_threeS_oneW_oneR()
    r = returns[4]
    c = returns[5]
    assert r.outputs['gfp'] == False
    c.simulate('iptg')

#End to end testing
def test_circuit_many_senders_to_one_wire2():
    returns = create_circuit_threeS_oneW_oneR()
    r = returns[4]
    c = returns[5]
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

#Edge Case Test
def test_circuit_with_no_input():
    sender = sim.Sender('iptg', 'ahl')
    circuit = sim.Circuit([sender])
    # The circuit with no input
    assert circuit.simulate([]) == False

