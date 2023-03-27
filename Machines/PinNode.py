from Machines.LinkedListElementsPin import LinkedListElementsPin

class PinNode:
    def __init__(self,index,listElements):
        self.index = index
        self.listElements : LinkedListElementsPin = listElements
        self.next = None
        self.prev = None