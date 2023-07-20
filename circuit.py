from cell import Cell
from sender import Sender
from receiver import Receiver
from wire import Wire
# Class where cells are represented as a graph
class Circuit:
    def __init__(self, start_cells):
        if not isinstance(start_cells, list):
            start_cells = [start_cells]
        self.signals = []
        self.cells = start_cells

    # Adds iptg to all cells
    def add_iptg(self, node = None, visited = None):
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

    # Read output of cell
    def read_output(self, Cell):
        if not Cell.to_cells:
            return Cell.outputs[Cell.signal_out]
        
        for tc in Cell.to_cells:
            if self.read_output(tc):
                return True
        
        return False
        
    # Run circuit
    def simulate(self, signal):
        out = False
        for c in self.cells:
            c.update(signal)
            out = out | self.read_output(c)
        return out
