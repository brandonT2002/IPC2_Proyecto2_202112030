from Machines.PinNode import PinNode

class LinkedListPins:
    def __init__(self):
        self.first = None
        self.last = None

    def insertListElements(self,listElements):
        if self.first:
            self.last.next = PinNode(listElements)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = PinNode(listElements)
        self.last = self.first

    def iteratedList(self):
        current = self.first
        while current:
            print('Pin:',current.index)
            print('Elementos',current.listElements.iteratedList())
            current = current.next