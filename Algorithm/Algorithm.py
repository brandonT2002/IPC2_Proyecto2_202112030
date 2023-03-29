from Machines.Machine import Machine
from Machines.LinkedListElementsPin import LinkedListElementsPin
from Compounds.LinkedListElementsComp import LinkedListElementsComp
from Algorithm.Coordinate import Coord

class Algorithm:
    def __init__(self,machine):
        self.machine : Machine = machine

    def buildElement(self,compound : LinkedListElementsComp) -> bool:
        found : Coord
        element = compound.first
        while element:
            print(element.element)
            found = self.getCoordinate(element.element)
            if found:
                self.movePins(found.pin,found.element)
            else:
                print(element.element,'retorna falso')
                return False
            element = element.next
        #resetear pines
        return True

    def movePins(self,pinY,elmX):
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
                    print('fusiona:','pin =',pinY,'elemento =',elmX)
                    pass
                else:
                    if right:
                        pin.listElements.moveRight()
                    else:
                        pin.listElements.moveLeft()
            else:
                if pin.index == pinY:
                    print('fusiona:','pin =',pinY,'elemento =',elmX)
            pin = pin.next

    def getCoordinate(self,element):
        for j in range(self.machine.sizeElements()):
            for i in range(self.machine.size()):
                pin = self.machine.getPin(i)
                elm = pin.listElements.get(j)
                if elm.element.symbol == element:
                    return Coord(i,j)
        return None