import sim   # The code to test
import pytest

def create_Circuit_oneS_oneW_oneR():
    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()
    return [s, w, r, c]

def create_Circuit_oneS_twoW_twoR():
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

def create_Circuit_twoS_twoW_oneR():
    sender1 = sim.Sender('iptg', 'ahl')
    sender2 = sim.Sender('iptg', 'ahl')
    Receiver = sim.Receiver(['iptg', 'ahl'], 'gfp')
    Wire1 = sim.Wire('ahl')
    Wire2 = sim.Wire('ahl')
    sender1.connect(Wire1)
    Wire1.connect(Receiver)
    sender2.connect(Wire2)
    Wire2.connect(Receiver)
    Circuit = sim.Circuit([sender1, sender2])
    Circuit.add_iptg()
    return Circuit

    

def create_Circuit_threeS_NineW_threeR():
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

def create_Circuit_oneS_oneW_threeR():
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

def create_Circuit_threeS_oneW_oneR():
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
def test_Wire_simple1():
    Wire = sim.Wire('iptg')
    Wire.update(['iptg'])
    assert Wire.inputs['iptg'] and Wire.outputs['iptg'] == True

#Simple unit test
def test_Wire_simple2():
    Wire = sim.Wire('ahl')
    Wire.logic(['ahl'])
    assert Wire.inputs['ahl'] and Wire.inputs['ahl'] == True

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
def test_Receiver_simple1():
    Receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Receiver.update(['ahl', 'iptg'])
    assert Receiver.inputs['ahl'] and Receiver.inputs['iptg'] and Receiver.outputs['gfp'] == True

#Simple unit test
def test_Receiver_simple2():
    Receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Receiver.logic(['ahl', 'iptg'])
    assert Receiver.inputs['ahl'] and Receiver.inputs['iptg'] and Receiver.outputs['gfp'] == True
    

#Integration test
def test_cell_connection_SR():
    send_cell = sim.Sender('iptg', 'ahl')
    Receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    send_cell.connect(Receiver_cell)
    assert Receiver_cell in send_cell.to_cells and send_cell in Receiver_cell.from_cells

#Integration test
def test_cell_connection_SW():
    send_cell = sim.Sender('iptg', 'ahl')
    Wire = sim.Wire('iptg')
    send_cell.connect(Wire)
    assert Wire in send_cell.to_cells and send_cell in Wire.from_cells

#Integration test
def test_cell_connection_WR():
    Wire = sim.Wire('iptg')
    Receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Wire.connect( Receiver_cell)
    assert Receiver_cell in Wire.to_cells and Wire in Receiver_cell.from_cells

#Integration test
def test_cell_connection_WS():
    Wire = sim.Wire('iptg')
    send_cell = sim.Sender('iptg', 'ahl')
    Wire.connect(send_cell)
    assert send_cell in Wire.to_cells and Wire in send_cell.from_cells

#Integration test
def test_cell_connection_RW():
    Receiver_cell = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Wire = sim.Wire('iptg')
    Receiver_cell.connect(Wire)
    assert Wire in Receiver_cell.to_cells and Receiver_cell in Wire.from_cells


#Functional Test
def test_Circuit_simulation1():
    sender = sim.Sender('iptg', 'ahl')
    Receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    sender.connect(Receiver)
    Circuit = sim.Circuit(sender)
    Circuit.add_iptg()
    assert Circuit.simulate(['iptg']) == True

#Functional Test
def test_Circuit_simulation2():
    sender = sim.Sender('iptg', 'ahl')
    Wire = sim.Wire('iptg')
    sender.connect(Wire)
    Circuit = sim.Circuit(sender)
    Circuit.add_iptg()
    assert Circuit.simulate(['iptg']) == True

#End to end testing
def test_end_to_end_simulation1():
    Circuit = create_Circuit_oneS_oneW_oneR()[3]
    assert Circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation2():
    Circuit = create_Circuit_oneS_twoW_twoR()[5]
    assert Circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation3():
    Circuit = create_Circuit_twoS_twoW_oneR()
    assert Circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation4():
    Circuit = create_Circuit_threeS_NineW_threeR()[15]
    Circuit.add_iptg()
    assert Circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation5():
    Circuit = create_Circuit_oneS_oneW_threeR()[5]
    assert Circuit.simulate(['iptg', 'ahl']) == True

#End to end testing
def test_end_to_end_simulation6():
    Circuit = create_Circuit_threeS_oneW_oneR()[5]    
    assert Circuit.simulate(['iptg', 'ahl']) == True


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
    sender = sim.Sender('iptg', 'ahl')
    Circuit = sim.Circuit([sender])
    # The Circuit with no input
    assert Circuit.simulate([]) == False

#Edge Case Test
def test_Circuit_with_wrong_input():
    sender = sim.Sender('iptg', 'ahl')
    Circuit = sim.Circuit([sender])
    # The Circuit with no input
    assert Circuit.simulate(['gfp']) == False

#Edge Case Test
def test_cell_connection_SS():
    send_cell1 = sim.Sender('iptg', 'ahl')
    send_cell2 = sim.Sender('iptg', 'ahl')
    send_cell1.connect(send_cell2)
    assert send_cell2 in send_cell1.to_cells and send_cell1 in send_cell2.from_cells

#Edge Case Test
def test_cell_connection_WW():
    Wire1 = sim.Wire('iptg')
    Wire2 = sim.Wire('iptg')
    Wire1.connect(Wire2)
    assert Wire2 in Wire1.to_cells and Wire1 in Wire2.from_cells

#Edge Case Test
def test_cell_connection_RR():
    Receiver_cell1 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Receiver_cell2 = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Receiver_cell1.connect(Receiver_cell2)
    assert Receiver_cell2 in Receiver_cell1.to_cells and Receiver_cell1 in Receiver_cell2.from_cells

#Edge Case Test
def test_Wire_edge1():
    Wire = sim.Wire('iptg')
    Wire.update(['ahl'])
    assert Wire.inputs['iptg'] == False and Wire.outputs['iptg'] == False

#Edge Case Test
def test_Wire_edge2():
    Wire = sim.Wire('ahl')
    Wire.logic(['iptg'])
    assert Wire.inputs['ahl'] == False and Wire.inputs['ahl'] == False

#Edge Case Test
def test_sender_edge1():
    sender = sim.Sender('iptg', 'ahl')
    sender.update(['ahl'])
    assert sender.inputs['iptg'] == False and sender.outputs['ahl'] == False

#Edge Case Test
def test_sender_edge2():
    sender = sim.Sender('iptg', 'ahl')
    sender.logic(['ahl'])
    assert sender.inputs['iptg'] == False and sender.outputs['ahl'] == False

#Edge Case Test
def test_Receiver_edge1():
    Receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Receiver.update(['gfp'])
    assert Receiver.inputs['ahl'] == False and Receiver.inputs['iptg'] == False and Receiver.outputs['gfp'] == False

#Edge Case Test
def test_Receiver_edge2():
    Receiver = sim.Receiver(['ahl', 'iptg'], 'gfp')
    Receiver.logic(['gfp'])
    assert Receiver.inputs['ahl'] == False and Receiver.inputs['iptg'] == False and Receiver.outputs['gfp'] == False

