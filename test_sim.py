import sim   # The code to test
import pytest

def test_circuit_start():
    s = sim.Sender()
    r = sim.Receiver()
    s.connect(r)
    c = sim.Circuit([s])
    c.iptg_signal(True)
    assert c.get_gfp() == True

'''
These two test shows that there is something broken in the code. This code creates a circuit
with one sender and two recievers. When the first reciever does not produce gfp but the second
one does, get_gfp() returns False instead of True. However, when the first reciever does produce gfp
but the second one doesn't, get_gfp() returns True like its supposed to.

'''

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


def test_wire():
    '''
    s = sim.Sender()
    r = sim.Receiver()
    w = sim.Wire()
    Connect wire to sender and receiver
    c = sim.Circuit([s])
    c.iptg_signal(True)
    assert c.get_gfp() == True
    '''
    assert True

def test_no_receiver():
    '''
    s = sim.Sender()
    w = sim.Wire()
    Connect wire to send
    c = sim.Circuit([s])
    c.iptg_signal(True)
    assert c.get_gfp() == False
    '''
    assert True