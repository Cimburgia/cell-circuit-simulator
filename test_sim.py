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



#Test simple circuit with one sender, one wire, and one receiver
def test_circuit_one1():
    returns = create_circuit_oneS_oneW_oneR()
    c = returns[3]
    r = returns[2]
    assert r.outputs['gfp'] == False
    c.simulate('iptg')
    

def test_circuit_one2():
    returns = create_circuit_oneS_oneW_oneR()
    c = returns[3]
    r = returns[2]
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

#Test circuit with one sender, two wires, and two receiver
def test_circuit_two1():
    returns = create_circuit_oneS_twoW_twoR()
    c = returns[5]
    r = returns[3]
    r1 = returns[4]
    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False
    c.simulate('iptg')

def test_circuit_two2():
    returns = create_circuit_oneS_twoW_twoR()
    c = returns[5]
    r = returns[3]
    r1 = returns[4]
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] == True

#Test circuit with 3 senders, 9 wires, and three receivers
def test_circuit_three1():
    returns = create_circuit_threeS_NineW_threeR()
    c = returns[15]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
    c.simulate('iptg')

def test_circuit_three2():
    returns = create_circuit_threeS_NineW_threeR()
    c = returns[15]
    r = returns[12]
    r1 = returns[13]
    r2 = returns[14]
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True

#Test readOutput with one sender, one wire, and one receiver
def test_read_output_one1():
    returns = create_circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    assert c.read_output(s) == False and c.read_output(w) == False and c.read_output(r) == False
    c.simulate('iptg')

def test_read_output_one2():
    returns = create_circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    c.simulate('iptg')
    assert c.read_output(s) and c.read_output(w) and c.read_output(r) == True



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

'''
These two test shows that there is something broken in the code. This code creates a circuit
with one sender and two recievers. When the first reciever does not produce gfp but the second
one does, get_gfp() returns False instead of True. However, when the first reciever does produce gfp
but the second one doesn't, get_gfp() returns True like its supposed to.


def test_get_gfp1():
    s = sim.Sender()
    r = sim.Receiver()
    r1 = sim.Receiver()
    s.connect(r)
    s.connect(r1)
    c = sim.Circuit([s])
    c.iptg_signal(True)
    r.outputs['gfp'] = False
    assert c.get_gfp() == True


def test_get_gfp2():
    s = sim.Sender()
    r = sim.Receiver()
    r1 = sim.Receiver()
    s.connect(r)
    s.connect(r1)
    c = sim.Circuit([s])
    c.iptg_signal(True)
    r1.outputs['gfp'] = False
    assert c.get_gfp() == True
'''



def test_wire():
    returns = create_circuit_oneS_oneW_oneR()
    s = returns[0]
    w = returns[1]
    r = returns[2]
    c = returns[3]

    c.simulate('iptg')
    assert w.inputs['ahl'] and w.outputs['ahl'] == True
    
'''
s.inputs['iptg'] returns True, but s1.inputs['iptg'] and s1.inputs['iptg'] return False
s is connected to w, w1, and w2, so w.inputs['iptg'], w1.inputs['iptg'], and w2.inputs['iptg'] all return True
s1 is connected to w3, w4, and w5, so w3.inputs['iptg'], w4.inputs['iptg'], and w5.inputs['iptg'] cause an error when code is ran.

'''

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


#Test simple circuit with one sender, and one wire that connects to 3 recievers
def test_circuit_one_wire_to_many_recievers1():
    returns = create_circuit_oneS_oneW_threeR()
    r = returns[2]
    r1 = returns[3]
    r2 = returns[4]
    c = returns[5]

    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
    c.simulate('iptg')

def test_circuit_one_wire_to_many_recievers2():
    returns = create_circuit_oneS_oneW_threeR()
    r = returns[2]
    r1 = returns[3]
    r2 = returns[4]
    c = returns[5]

    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True


#Test simple circuit with one sender, and one wire that connects to 3 recievers
def test_circuit_many_senders_to_one_wire1():
    returns = create_circuit_threeS_oneW_oneR()
    r = returns[4]
    c = returns[5]
    assert r.outputs['gfp'] == False
    c.simulate('iptg')

def test_circuit_many_senders_to_one_wire2():
    returns = create_circuit_threeS_oneW_oneR()
    r = returns[4]
    c = returns[5]
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

'''


-Do we need to create get_gfp() function? If yes, create tests for it like before

'''
print("test")