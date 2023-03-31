from Machines.Machine import Machine

class Step:
    def __init__(self,index,machine,pinY,elmX):
        self.index = index
        self.machine : Machine = machine
        self.pinY = pinY
        self.elmX = elmX
        self.next = None
        self.prev = None

class Steps:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def cloneMachine(self,machine : Machine) -> Machine:
        newMachine = Machine()
        current = machine.first
        while current:
            newMachine.first.index = current.index
            newMachine.first.listElements = current.listElements
            current = current.next
        return newMachine

    def insert(self,machine,pinY = -1,elmX = -1):
        if self.first:
            self.last.next = Step(self.index,self.cloneMachine(machine),pinY,elmX)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = Step(self.index,self.cloneMachine(machine),pinY,elmX)
        self.last = self.first
        self.index += 1