import random
from Machines.Machine import Machine

class Step:
    def __init__(self,index,machine,pinY,elmX):
        self.index = index
        self.machine : Machine = machine
        self.pinY = pinY
        self.elmX = elmX
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'pinY = {self.pinY} - elmX = {self.elmX}'

class Steps:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0
        self.colorsRow = ColorList()

    def insert(self,machine : Machine,pinY = -1,elmX = -1):
        if self.first:
            if not self.exist(machine,pinY,elmX):
                self.last.next = Step(self.index,machine.clone(),pinY,elmX)
                self.last.next.prev = self.last
                self.last = self.last.next
                self.index += 1
            else:
                self.last.machine = machine.clone()
                self.last.pinY = pinY
                self.last.elmX = elmX
            return
        self.first = Step(self.index,machine.clone(),pinY,elmX)
        self.last = self.first
        self.index += 1
        self.createColors()

    def exist(self,machine : Machine,pinY,elmX):
        if self.index > 1:
            lastMachine = self.last.machine
            for i in range(machine.size()):
                if lastMachine.getPin(i).listElements.getCurrent():
                    if lastMachine.getPin(i).listElements.getCurrent().index != machine.getPin(i).listElements.getCurrent().index:
                        return False
            if pinY != -1 and elmX != -1:
                return True
        return False

    def iterated(self):
        current = self.first
        while current:
            current = current.next

    def getDot(self):
        current = self.first
        dot = 'digraph pasos {\nrankdir = TB;\n'
        while current:
            dot += f'{current.machine.getStep(current.index,current.pinY,current.elmX,self.colorsRow)}'
            current = current.next
            if current:
                dot += f'node{current.prev.index} -> node{current.index}[style=invis];\n'
        dot += '}'
        return dot

    def createColors(self):
        self.colorsRow.insert('#B9E0FF')
        self.colorsRow.insert('#8D9EFF')
        self.colorsRow.insert('#8D72E1')
        self.colorsRow.insert('#D2D79F')
        self.colorsRow.insert('#90B77D')
        self.colorsRow.insert('#FFEA11')
        self.colorsRow.insert('#FAAB78')
        self.colorsRow.insert('#FFD495')
        self.colorsRow.insert('#FFFBAC')
        self.colorsRow.insert('#2192FF')
        self.colorsRow.insert('#38E54D')
        self.colorsRow.insert('#9CFF2E')
        self.colorsRow.insert('#FDFF00')
        self.colorsRow.insert('#FFF38C')
        self.colorsRow.insert('#F0E161')
        self.colorsRow.insert('#D9CB50')
        self.colorsRow.insert('#C0B236')
        self.colorsRow.insert('#E3FCBF')
        self.colorsRow.insert('#B8F1B0')
        self.colorsRow.insert('#14C38E')
        self.colorsRow.insert('#00FFAB')
        self.colorsRow.insert('#FFA1A1')
        self.colorsRow.insert('#FFD59E')
        self.colorsRow.insert('#F9FFA4')
        self.colorsRow.insert('#B4FF9F')
        self.colorsRow.insert('#DAF5FF')
        self.colorsRow.insert('#B9E9FC')
        self.colorsRow.insert('#C3F8FF')
        self.colorsRow.insert('#B0DAFF')
        self.colorsRow.insert('#B2A4FF')
        self.colorsRow.insert('#DEF5E5')
        self.colorsRow.insert('#BCEAD5')
        self.colorsRow.insert('#9ED5C5')
        self.colorsRow.insert('#8EC3B0')
        self.colorsRow.insert('#F5F3C1')
        self.colorsRow.insert('#27E1C1')
        self.colorsRow.insert('#FFD93D')
        self.colorsRow.insert('#B2A4FF')
        self.colorsRow.insert('#7AA874')
        self.colorsRow.insert('#62CDFF')
        self.colorsRow.insert('#FFA3FD')
        self.colorsRow.insert('#BFDB38')
        self.colorsRow.insert('#F1F6F5')
        self.colorsRow.insert('#FFD93D')
        self.colorsRow.insert('#88A47C')
        self.colorsRow.insert('#D7E9B9')
        self.colorsRow.insert('#82C3EC')
        self.colorsRow.insert('#E7B10A')

class Color:
    def __init__(self,index,color) -> None:
        self.index = index
        self.color = color
        self.next = None
        self.prev = None

class ColorList:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,color):
        if self.first:
            self.last.next = Color(self.index,color)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = Color(self.index,color)
        self.last = self.first
        self.index += 1

    def get(self,index):
        current = self.first
        while current:
            if current.index == index:
                return current.color
            current = current.next
        return None

    def size(self):
        return self.index