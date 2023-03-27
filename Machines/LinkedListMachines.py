from Machines.MachineNode import MachineNode

class LinkedListMachines:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,name,numPins,numElements,machine):
        if self.first:
            self.last.next = MachineNode(self.index,name,numPins,numElements,machine)
            self.last.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = MachineNode(self.index,name,numPins,numElements,machine)
        self.last = self.first
        self.index += 1

    def iterated(self):
        current = self.first
        while current:
            print(f'{current.index}. {current.name}')
            print('Pines:',current.numPins,'Elementos:',current.numElements)
            current.machine.iterated()
            current = current.next

    def getDot(self,index):
        current = self.first
        while current:
            if current.index == index:
                current.machine.getDot()
                return
            current = current.next