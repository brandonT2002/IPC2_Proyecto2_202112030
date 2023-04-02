from Compounds.CompoundNode import CompoundNode

class LinkedListCompounds:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,name,elements):
        if self.first:
            self.last.next = CompoundNode(self.index,name,elements)
            self.last.prev = self.last
            self.last = self.last.next
            self.index += 1
        self.first = CompoundNode(self.index,name,elements)
        self.last = self.first
        self.index += 1

    def iterated(self):
        current = self.first
        while current:
            print(f'{current.index}. {current.name}')
            current.elements.iterated()
            current = current.next

    def getCompound(self,index):
        current = self.first
        while current:
            if current.index == index:
                return current
            current = current.next