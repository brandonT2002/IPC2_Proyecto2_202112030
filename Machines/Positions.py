from Machines.Position import Position

class Positions:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,element,pinY,elmX):
        if self.first:
            self.last.next = Position(self.index,element,pinY,elmX)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = Position(self.index,element,pinY,elmX)
        self.last = self.first
        self.index += 1

    def iterated(self):
        current = self.first
        while current:
            print('*',current.element)
            print('-fusiona:','pin =',current.pinY,'elemento =',current.elmX)
            current = current.next