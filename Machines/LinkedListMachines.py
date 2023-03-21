from Machines.MachineNode import MachineNode

class LinkedListMachines:
    def __init__(self):
        self.first = None
        self.last = None

    def insertListPins(self,listPins):
        if self.first:
            self.last.next = MachineNode(listPins)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = MachineNode(listPins)
        self.last = self.first

    def iteratedList(self):
        current = self.first
        while current:
            print(current.index,current.name)
            print(current.numPins,current.numElements)
            current.listPins.iteratedList()
            current = current.next