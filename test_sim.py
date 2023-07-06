import sim   # The code to test
import pytest

#Test simple circuit with one sender, one wire, and one receiver
def test_circuit_one():

    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()

    assert r.outputs['gfp'] == False
    c.simulate('iptg')
    assert r.outputs['gfp'] == True

#Test circuit with one sender, two wires, and two receiver
def test_circuit_two():
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

    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] == True

#Test circuit with 3 senders, 9 wires, and three receivers
def test_circuit_three():
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


    c = sim.Circuit(s)

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


    c.add_iptg()

    assert r.outputs['gfp'] == False and r1.outputs['gfp'] == False and r2.outputs['gfp'] == False
    c.simulate('iptg')
    assert r.outputs['gfp'] and r1.outputs['gfp'] and r2.outputs['gfp'] == True

#Test readOutput with one sender, one wire, and one receiver
def test_read_output_one():

    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()

    assert c.read_output(s) == False and c.read_output(w) == False and c.read_output(r) == False
    c.simulate('iptg')
    assert c.read_output(s) and c.read_output(w) and c.read_output(r) == True

#Test readOutput with one sender, two wires, and two receivers
#This test failed because c.read_output(s) is True instead of false before c.simulate('iptg') is ran. 
def test_read_output_two():

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

    assert c.read_output(s) == False and c.read_output(w) == False and c.read_output(w1) == False and c.read_output(r) == False and c.read_output(r1) == False
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
    s = sim.Sender('iptg', 'ahl')
    w = sim.Wire('ahl')
    r = sim.Receiver(['ahl', 'iptg'], 'gfp')

    c = sim.Circuit(s)

    s.connect(w)
    w.connect(r)

    c.add_iptg()

    c.simulate('iptg')
    assert w.inputs['ahl'] and w.outputs['ahl'] == True
    
def test_add_iptg():
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


    c = sim.Circuit(s)

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


    c.add_iptg()

    assert s.inputs['iptg'] and s1.inputs['iptg'] and s2.inputs['iptg'] and w.inputs['iptg'] and w1.inputs['iptg'] and w2.inputs['iptg']  and w3.inputs['iptg'] and w4.inputs['iptg'] and w5.inputs['iptg'] and w6.inputs['iptg'] and w7.inputs['iptg'] and w8.inputs['iptg'] and r.inputs['iptg'] and r1.inputs['iptg'] and r2.inputs['iptg'] == True
    
'''
1.Test to make sure that all cells have IPTG after c.addIptg() and don't have IPTG before it


-What does readOutput function do?
-Is there get_gfp() function? If yes, create tests for it like before
-Where there is no c.add_iptg(), w.inputs['iptg'] gives error
'''
