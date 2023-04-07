from Compounds.LinkedListElementsComp import LinkedListElementsComp

class CompoundNode:
    def __init__(self,index,name,elements):
        self.index = index
        self.name = name
        self.elements : LinkedListElementsComp = elements
        self.next = None
        self.prev = None