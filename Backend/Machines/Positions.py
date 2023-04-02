from Machines.Position import Position

class Positions:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0
        self.pinsID = IDS()

    def insert(self,element,pinY,elmX):
        if self.first:
            self.last.next = Position(self.index,element,pinY,elmX)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            self.pinsID.insert(pinY)
            return
        self.first = Position(self.index,element,pinY,elmX)
        self.last = self.first
        self.index += 1
        self.pinsID.insert(pinY)

    def pop(self):
        pop = self.first
        self.first = self.first.next
        self.index -= 1
        current = self.first
        while current:
            current.index -= 1
            current = current.next
        return pop

    def isEmpty(self):
        return not self.first

    def size(self):
        return self.index

    def get(self,index) -> Position:
        current = self.first
        while current:
            if current.index == index:
                return current
            current = current.next

    def iterated(self):
        current = self.first
        while current:
            print(current)
            current = current.next

class IDS:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,pinY):
        if self.first:
            if not self.__existID(pinY):
                self.last.next = Position(self.index,-1,pinY,-1)
                self.last.next.prev = self.last
                self.last = self.last.next
                self.index += 1
            return
        self.first = Position(self.index,-1,pinY,-1)
        self.last = self.first
        self.index += 1

    def __existID(self,id):
        current = self.first
        while current:
            if current.pinY == id:
                return True
            current = current.next
        return False

    def get(self,index):
        current = self.first
        while current:
            if current.index == index:
                return current
            current = current.next

    def size(self):
        return self.index