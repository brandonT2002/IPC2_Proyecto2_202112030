from Machines.PinNode import PinNode

class Machine:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,listElements):
        if self.first:
            self.last.next = PinNode(self.index,listElements)
            self.last.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = PinNode(self.index,listElements)
        self.last = self.first
        self.index += 1

    def iterated(self):
        current = self.first
        while current:
            print('Pin:',current.index)
            current.listElements.iterated()
            current = current.next