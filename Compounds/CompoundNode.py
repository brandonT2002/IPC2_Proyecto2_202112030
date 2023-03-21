class CompoundNode:
    def __init__(self,index,name,elements):
        self.index = index
        self.name = name
        self.elements = elements
        self.next = None
        self.prev = None