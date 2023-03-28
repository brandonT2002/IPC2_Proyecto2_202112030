from Machines.Machine import Machine
from Machines.LinkedListElementsPin import LinkedListElementsPin
from Compounds.LinkedListElementsComp import LinkedListElementsComp
from Algorithm.Coordinate import Coordinate

class Algorithm:
    def __init__(self,machine):
        self.machine : Machine = machine

    def buildElement(self,compound : LinkedListElementsComp) -> bool:
        found : Coordinate
        for element in compound:
            found = self.getCoordinate(element)
            if found != None:
                self.movePins()
            else:
                return False
        #resetear pines
        return True

    def movePins(self,pinY,elmX):
        right : bool
        stop : bool
        for pin in self.machine:
            stop = pin.getCurrent().index == elmX
            if not stop:
                right = pin.getCurrent().index < elmX
                while True:
                    if right:
                        pin.moveRight()
                    else:
                        pin.moveLeft()
                    if pin.getCurrent().index == elmX:
                        break
                if pin.index == pinY:
                    #fusionar
                    pass
                else:
                    if right:
                        pin.moveRight()
                    else:
                        pin.moveLeft()

    def getCoordinate(self,element) -> Coordinate:
        index : int
        for pin in self.machine:
            index = self.searchElement(element)
            if index != -1:
                return Coordinate(pin.index,index)
        return None

    def searchElement(self,element):
        for j in range(self.machine.sizeElements()):
            for i in range(self.machine.size()):
                pin = self.machine.getPin(i)
                element = pin.listElements.get(j)
                if element.element.name == element:
                    return element.index
        return -1