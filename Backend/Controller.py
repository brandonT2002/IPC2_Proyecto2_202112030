from Read import Read
from Backend.Elements.LinkedListElements import LinkedListElements
from Backend.Machines.LinkedListMachines import LinkedListMachines
from Backend.Compounds.LinkedListCompounds import LinkedListCompounds
import json

class Controller:
    def __init__(self) -> None:
        self.llElements = LinkedListElements()
        self.llMachines = LinkedListMachines()
        self.llCompounds = LinkedListCompounds()

    def upload(self,path):
        read = Read()
        read.readFile(path)

        print('\nElementos')
        self.llElements : LinkedListElements = read.getElements(self.llElements)
        self.llElements.iterated()

        print('\nMaquinas')
        self.llMachines : LinkedListMachines = read.getMachines(self.llElements,self.llMachines)
        self.llMachines.iterated()

        print('\nCompuestos')
        self.llCompounds : LinkedListCompounds = read.getCompounds(self.llCompounds)
        self.llCompounds.iterated()

        return json({"msg":"Archivo cargado exitosamente"}),200