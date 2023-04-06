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

        self.llElements : LinkedListElements = read.getElements(self.llElements)
        self.llMachines : LinkedListMachines = read.getMachines(self.llElements,self.llMachines)
        self.llCompounds : LinkedListCompounds = read.getCompounds(self.llCompounds)

        return jsonify({"msg":"Archivo cargado exitosamente"}),200

    def getDotM(self,index):
        dot = self.llMachines.getDot(index)
        if dot:
            return jsonify({"msg":dot}),200
        return jsonify({"msg":"No hay datos cargados"})

    def getElementsJSON(self):
        current = self.llElements.first
        json = []
        while current:
            json.append(current.element.__dict__)
            current = current.next
        return json

    def getElements(self):
        self.llElements.sort()
        return jsonify(self.getElementsJSON()),200