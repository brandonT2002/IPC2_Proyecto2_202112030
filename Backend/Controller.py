import csv
from Read import Read
from Elements.LinkedListElements import LinkedListElements
from Machines.LinkedListMachines import LinkedListMachines
from Compounds.LinkedListCompounds import LinkedListCompounds
from Elements.Element import Element
from Algorithm.Algorithm import Algorithm
from flask import Response

class Controller:
    def __init__(self) -> None:
        self.initObjects()

    def initObjects(self):
        self.llElements = LinkedListElements()
        self.llMachines = LinkedListMachines()
        self.llCompounds = LinkedListCompounds()
        return 'Sistema Restaurado',200

    def upload(self,content):
        try:
            read = Read()
            read.readFile(content)

            self.llElements : LinkedListElements = read.getElements(self.llElements)
            self.llMachines : LinkedListMachines = read.getMachines(self.llElements,self.llMachines)
            self.llCompounds : LinkedListCompounds = read.getCompounds(self.llCompounds)
            return 'Archivo cargado exitosamente',200
        except:
            return 'Archivo cargado exitosamente',200

    def getMachinesCSV(self):
        if not self.llMachines.first:
            return 'None'
        current = self.llMachines.first
        string_csv = ''
        while current:
            string_csv += f'{int(current.index) + 1},{current.name}'
            current = current.next
            if current: string_csv += '\n'
        return string_csv

    def getMachines(self):
        return Response(self.getMachinesCSV(),mimetype='text/csv'),200

    def getDotM(self,index):
        return self.llMachines.getDot(index),200

    def getElementsCSV(self):
        if not self.llElements.first:
            return 'None'
        current = self.llElements.first
        string_csv = ''
        while current:
            string_csv += current.element.getCSV()
            current = current.next
            if current: string_csv += '\n'
        return string_csv

    def getElements(self):
        self.llElements.sort()
        return Response(self.getElementsCSV(),mimetype='text/csv'),200

    def newElement(self,atomicNum,symbol,name):
        element = self.llElements.existElement(atomicNum,symbol,name)
        if not element:
            self.llElements.insert(Element(atomicNum,symbol,name))
            return 'Elemento registrado',200
        return 'El elemento ya existe',200

    def getCompoundsCSV(self):
        if not self.llCompounds.first:
            return 'None'
        current = self.llCompounds.first
        string_csv = ''
        while current:
            string_csv += f'{int(current.index) + 1},{current.name},{current.elements.getCSV()}'
            current = current.next
            if current: string_csv += '\n'
        return string_csv

    def getCompounds(self):
        return Response(self.getCompoundsCSV(),mimetype='text/csv'),200

    def getDotStep(self,machine,compound):
        machine = self.llMachines.getMachine(machine).machine
        compound = self.llCompounds.getCompound(compound).elements
        alg = Algorithm(machine)
        if alg.buildCompound(compound):
            return alg.steps.getDot(),200
        return 'No se puede construir',200