from Read import Read
from Elements.LinkedListElements import LinkedListElements
from Machines.LinkedListMachines import LinkedListMachines
from Compounds.LinkedListCompounds import LinkedListCompounds
from Elements.Element import Element
from Algorithm.Algorithm import Algorithm
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

    def getMachinesJSON(self):
        current = self.llMachines.first
        json = []
        while current:
            json.append({"index":current.index,"name":current.name})
            current = current.next
        return json

    def getMachines(self):
        return jsonify(self.getMachinesJSON()),200

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

    def newElement(self,atomicNum,symbol,name):
        element = self.llElements.existElement(atomicNum,symbol,name)
        if not element:
            self.llElements.insert(Element(atomicNum,symbol,name))
            return jsonify({"msg":"Elemento registrado"}),200
        return jsonify({"msg":"El elemento ya existe"}),200

    def getCompoundsJSON(self):
        current = self.llCompounds.first
        json = []
        while current:
            json.append({"index":current.index,"name":current.name})
            current = current.next
        return json

    def getCompounds(self):
        return jsonify(self.getCompoundsJSON()),200

    def getDotStep(self,machine,compound):
        machine = self.llMachines.getMachine(machine).machine
        compound = self.llCompounds.getCompound(compound).elements
        alg = Algorithm(machine)
        if alg.buildCompound(compound):
            return jsonify({"dot":alg.steps.getDot()}),200
        return jsonify({"dot":"No se puede construir"}),200