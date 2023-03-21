from Compounds.ElementCompNode import ElementCompNode

class LinkedListElementsComp:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self,element):
        if self.first:
            self.last.next = ElementCompNode(element)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = ElementCompNode(element)
        self.last = self.first

    def iterated(self):
        current = self.first
        while current:
            print(current.element)
            current = current.next