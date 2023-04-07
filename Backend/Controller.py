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
        self.llElements = LinkedListElements()
        self.llMachines = LinkedListMachines()
        self.llCompounds = LinkedListCompounds()

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
        current = self.llMachines.first
        string_csv = ''
        while current:
            string_csv += f'{current.index},{current.name}'
            current = current.next
            if current: string_csv += '\n'
        return string_csv

    def getMachines(self):
        return Response(self.getMachinesCSV(),mimetype='text/csv'),200

    def getDotM(self,index):
        return self.llMachines.getDot(index),200

    def getElementsCSV(self):
        current = self.llElements.first
        string_csv = ''
        while current:
            string_csv += current.element.getCSV()
            current = current.next
            if current: string_csv += '\n'
        return string_csv

    def getElements(self):
        self.llElements.sort()
        return Response(self.getElementsJSON(),mimetype='text/csv'),200

    def newElement(self,atomicNum,symbol,name):
        element = self.llElements.existElement(atomicNum,symbol,name)
        if not element:
            self.llElements.insert(Element(atomicNum,symbol,name))
            return 'Elemento registrado',200
        return 'El elemento ya existe',200

    def getCompoundsJSON(self):
        current = self.llCompounds.first
        string_csv = ''
        while current:
            string_csv += f'{current.index},{current.name}'
            current = current.next
            if current: string_csv += '\n'
        return string_csv

    def getCompounds(self):
        return Response(self.getCompoundsJSON(),mimetype='text/csv'),200

    def getDotStep(self,machine,compound):
        machine = self.llMachines.getMachine(machine).machine
        compound = self.llCompounds.getCompound(compound).elements
        alg = Algorithm(machine)
        if alg.buildCompound(compound):
            return alg.steps.getDot(),200
        return 'No se puede construir',200