from Read import Read
from Elements.LinkedListElements import LinkedListElements
from Machines.LinkedListMachines import LinkedListMachines
from Compounds.LinkedListCompounds import LinkedListCompounds
from flask import jsonify

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

        return jsonify({"msg":"Archivo cargado exitosamente"}),200

    def getDotM(self,index):
        dot = self.llMachines.getDot(index)
        if dot:
            return jsonify({"msg":dot}),200
        return jsonify({"msg":"No hay datos cargados"})