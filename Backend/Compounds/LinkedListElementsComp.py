from Compounds.ElementCompNode import ElementCompNode

class LinkedListElementsComp:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,element):
        if self.first:
            self.last.next = ElementCompNode(self.index,element)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = ElementCompNode(self.index,element)
        self.last = self.first
        self.index += 1

    def size(self):
        return self.index

    def iterated(self):
        current = self.first
        while current:
            print(current.element)
            current = current.next