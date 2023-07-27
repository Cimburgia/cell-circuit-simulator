'''
A cell will be a gate that can perform a given funciton. These are nodes or verticies in 
our graph representation of a circuit

Cells will be defined by their type:
    - INPUT (sender)
    - OUTPUT (receiver)
    - NOR
Cells will have a group of neighbors:
    - From Wire(s)
    - To Wires(s)
    - From Cell(s)
    - To Cells(s)

'''

class Cell:
    def __init__(self):
        self.inputs = {}
        self.outputs = {}
        self.from_cells = []
        self.to_cells = []

    
    def update(self, signals_in):
        """
        Calls the logic operation on itself, which processes the 
        current inputs into outputs. Then looks at all its neighboring cells
        and calls update on them.
        """
        self.logic(signals_in)
        for tc in self.to_cells:
            tc.update(self.outputs)

    def connect(self, Cell):
        """
        Connects itself to another cell
        """
        self.to_cells.append(Cell)
        Cell.from_cells.append(self)
