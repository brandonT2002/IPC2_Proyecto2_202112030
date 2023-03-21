class MachineNode:
    def __init__(self,index,name,numPins,numElements,listPins):
        self.index = index
        self.name = name
        self.numPins = numPins
        self.numElements = numElements
        self.listPins = listPins
        self.next = None
        self.prev = None