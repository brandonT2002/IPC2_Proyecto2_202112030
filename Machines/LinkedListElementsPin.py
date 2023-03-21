from Machines.ElementPinNode import ElementNode

class LinkedListElementsPin:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self,element):
        if self.first:
            self.last.next = ElementNode(element)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = ElementNode(element)
        self.last = self.first

    def iterated(self):
        current = self.first
        while current:
            print('Elemento:',current.element)
            current = current.next