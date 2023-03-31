from Machines.Machine import Machine
from Machines.Positions import Positions
from Compounds.LinkedListElementsComp import LinkedListElementsComp
from Algorithm.Coordinate import Coord

class Algorithm:
    def __init__(self,machine):
        self.machine : Machine = machine
        self.positions = Positions()

    def buildElement(self,compound : LinkedListElementsComp) -> bool:
        found : Coord
        element = compound.first
        while element:
            found = self.getCoordinate(element.element)
            if found:
                self.positions.insert(element.element,found.pin,found.element)
            else:
                return False
            element = element.next
        #resetear pines
        #self.positions.iterated()
        # graficar inicial
        self.movePins(compound.size())
        return True

    def movePins(self,compoundSize):
        print('Máquina')
        print(self.machine)
        print()
        for i in range(self.positions.pinsID.size()):
            position = self.positions.pinsID.get(i)
            pin = self.machine.getPin(position.pinY)
            pin.listElements.startPin()
        print('INICIO DE LA FUSIÓN')
        print('Máquina')
        print(self.machine)
        print()
        while not self.positions.isEmpty():
            for i in range(self.positions.size()):
                position = self.positions.get(i)
                pin = self.machine.getPin(position.pinY)
                if pin.listElements.getCurrent().index < position.elmX:
                    if not pin.listElements.moved:
                        pin.listElements.moveRight()
                elif pin.listElements.getCurrent().index > position.elmX:
                    if not pin.listElements.moved:
                        pin.listElements.moveLeft()
                elif pin.listElements.getCurrent().index == position.elmX:
                    pin.listElements.moved = True
            print('=====================')
            print('Máquina')
            print(self.machine)
            print()
            position = self.positions.get(0)
            pin = self.machine.getPin(position.pinY)
            if pin.listElements.getCurrent().index == position.elmX:
                first = self.positions.pop()
                print('=====================')
                print('FUSIONA',first.element)
                print('Máquina')
                print(self.machine)
                print()
            self.machine.reset()

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

    def getDot(self):
        dot = 'digraph pasos {\nrankdir = TB;\n'
        dot += '}'





# Li Cr Gd Bi Sm