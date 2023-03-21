class MachineNode:
    def __init__(self,index,name,numPins,numElements,machine):
        self.index = index
        self.name = name
        self.numPins = numPins
        self.numElements = numElements
        self.machine = machine
        self.next = None
        self.prev = None