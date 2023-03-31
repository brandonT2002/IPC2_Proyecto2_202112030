from Machines.LinkedListElementsPin import LinkedListElementsPin

class PinNode:
    def __init__(self,index,listElements):
        self.index = index
        self.listElements : LinkedListElementsPin = listElements
        self.next = None
        self.prev = None

    def __str__(self):
        return 'Pin: {:<4} -> {}{}'.format(self.index,self.listElements,'\n' + ' ' * 13 + '    ' * self.listElements.getCurrent().index + '↑' if self.listElements.getCurrent() else '')