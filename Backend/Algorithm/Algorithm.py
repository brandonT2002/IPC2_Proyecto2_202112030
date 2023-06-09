from Machines.Machine import Machine
from Machines.Positions import Positions
from Machines.Steps import Steps
from Compounds.LinkedListElementsComp import LinkedListElementsComp
from Algorithm.Coordinate import Coord
class Algorithm:
    def __init__(self,machine):
        self.machine : Machine = machine
        self.positions = Positions()
        self.steps = Steps()

    def buildCompound(self,compound : LinkedListElementsComp) -> bool:
        found : Coord
        element = compound.first
        while element:
            found = self.getCoordinate(element.element)
            if found:
                self.positions.insert(element.element,found.pin,found.element)
            else:
                return False
            element = element.next
        self.movePins()
        self.machine.reset()
        return True

    def movePins(self):
        self.steps.insert(self.machine)
        # inicializa una sola vez cada pin en el que haya un elemento del compuesto
        for i in range(self.positions.pinsID.size()):
            position = self.positions.pinsID.get(i)
            pin = self.machine.getPin(position.pinY)
            pin.listElements.startPin()
        self.steps.insert(self.machine)
        # mientras haya elementos para fusionar
        while not self.positions.isEmpty():
            for i in range(self.positions.size()):
                position = self.positions.get(i)
                pin = self.machine.getPin(position.pinY)
                if pin.listElements.getCurrent().index < position.elmX and not pin.listElements.moved:
                    pin.listElements.moveRight()
                elif pin.listElements.getCurrent().index > position.elmX and not pin.listElements.moved:
                    pin.listElements.moveLeft()
                elif pin.listElements.getCurrent().index == position.elmX and not pin.listElements.moved:
                    pin.listElements.moved = True
            self.steps.insert(self.machine)
            position = self.positions.get(0)
            pin = self.machine.getPin(position.pinY)
            if pin.listElements.getCurrent().index == position.elmX:
                first = self.positions.pop()
                self.steps.insert(self.machine,first.pinY,first.elmX)
            self.machine.resetMoves()

    def getCoordinate(self,element):
        for j in range(self.machine.sizeElements()):
            for i in range(self.machine.size()):
                pin = self.machine.getPin(i)
                elm = pin.listElements.get(j)
                if elm.element.symbol == element:
                    return Coord(i,j)
        return None

    def table(self,id,pinY,elmX):
        dot = f'node{id} [shape=none group="0" margin=0, label=\n<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">'
        dot += f'<tr>\n<td border="0">Paso {id}</td>\n</tr>'
        for j in range(self.machine.sizeElements()):
            dot += f'<tr>'
            for i in range(self.machine.size()):
                pin = self.machine.getPin(i)
                elm = pin.listElements.get(j)
                if pin.index == pinY and elm.index == elmX:
                    dot += f'<td BGCOLOR="gray" width="60" height="30">{elm.element.symbol}</td>\n'
                else:
                    dot += f'<td BGCOLOR="white" width="60" height="30">{elm.element.symbol}</td>\n'
            dot += f'</tr>\n'
        dot += '</TABLE>\n'
        dot += '];\n'

    def getSeconds(self):
        return self.steps.index - 1

    def getTime(self):
        return f'{self.steps.index - 1}'