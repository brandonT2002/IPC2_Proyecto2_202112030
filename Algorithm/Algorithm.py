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
                self.movePins(element.element,found.pin,found.element)
            else:
                print(element.element,'retorna falso')
                return False
            element = element.next
        #resetear pines
        self.positions.iterated()
        return True

    def movePins(self,element,pinY,elmX):
        right : bool
        stop : bool
        pin = self.machine.first
        while pin:
            stop = pin.listElements.getCurrent().index == elmX
            if not stop:
                right = pin.listElements.getCurrent().index < elmX
                while True:
                    if right:
                        pin.listElements.moveRight()
                    else:
                        pin.listElements.moveLeft()
                    if pin.listElements.getCurrent().index == elmX:
                        break
                if pin.index == pinY:
                    self.positions.insert(element,pinY,elmX)
            else:
                if pin.index == pinY:
                    self.positions.insert(element,pinY,elmX)
            pin = pin.next

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