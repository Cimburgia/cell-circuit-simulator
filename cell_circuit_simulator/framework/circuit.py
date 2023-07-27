from framework.sender import Sender
from framework.receiver import Receiver
from framework.wire import Wire

"""

Circuits will be represented as undirected graphs that contain cells connected by 
wires.
Levels:
- Abstract, no decisions on paramerters and for now human compiled
- Assigned, uses statistical models and user defined parameters to compile

Functions to add:
    - Circuit.get_outputs() [need to call build before we get full list]
    - Circuit.build_circuit()
    - Wire to be created when Cell.connect is called
    - Circuit.get_wires(built_circuit) -> list of wires
"""
class Circuit:
    def __init__(self, start_cells):
        if not isinstance(start_cells, list):
            start_cells = [start_cells]
        self.signals = []
        self.cells = start_cells

    def add_iptg(self, node = None, visited = None):
        """Traverses circuit and adds IPTG signal to each cell. This can be changed to 
        get a list of all cells and wires and return them"""
        if visited is None:
            visited = set()
        if node is None:
            for c in self.cells:
                self.add_iptg(c, visited)
        else:
            visited.add(node)
            node.inputs['iptg'] = True
            for tc in node.to_cells:
                if tc not in visited:
                    self.add_iptg(tc, visited)

    def read_output(self, Cell):
        """Returns the output of the circuit
        note: We can eventually just build the circuit and look at the out cells
        """
        if not Cell.to_cells:
            return Cell.outputs[Cell.signal_out]
        
        for tc in Cell.to_cells:
            if self.read_output(tc):
                return True
        
        return False
        
    def simulate(self, signal):
        """Runs a simulation on the circuit. Will eventually add 
        in modeling features
        Note: this currently just returns a boolean value which is the output of the circuit, 
        eventually it will return an expected signal strength at varying timepoints"""
        out = False
        for c in self.cells:
            c.update(signal)
            out = out | self.read_output(c)
        return out
    
    def build_circuit():
        """This function will reconstruct the circuit and return an 
        adjacency matrix of boolean values that describe connections"""
        pass

    def get_cells():
        pass

    def get_wires():
        pass