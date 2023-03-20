from xml.dom import minidom
from Elements.Element import Element

class Read:
    def readFile(self,path):
        self.file = minidom.parse(path)
        listelements = self.file.getElementsByTagName('listaElementos')[0]
        self.elements = listelements.getElementsByTagName('elemento')

    def getElements(self,llElements):
        print('\nElementos')
        for element in self.elements:
            nAtom = element.getElementsByTagName('numeroAtomico')[0].firstChild.data
            symbol = element.getElementsByTagName('simbolo')[0].firstChild.data
            name = element.getElementsByTagName('nombreElemento')[0].firstChild.data
            llElements.insertElement(Element(nAtom,symbol,name))
        return llElements

    def getMachines(self):
        print('\nMaquinas')
        machines = self.file.getElementsByTagName('Maquina')
        for machine in machines:
            name = machine.getElementsByTagName('nombre')[0].firstChild.data
            numPins = machine.getElementsByTagName('numeroPines')[0].firstChild.data
            numElements = machine.getElementsByTagName('numeroElementos')[0].firstChild.data
            print(name)
            print('  Pines',numPins)
            print('  Elementos',numElements)
            pins = machine.getElementsByTagName('pin')
            for pin in pins:
                print(f'  Pin {pins.index(pin)}')
                elements = pin.getElementsByTagName('elemento')
                for element in elements:
                    element = element.firstChild.data
                    print('    ',element)
            print()

    def getCompounds(self):
        print('Compuestos')
        compounds = self.file.getElementsByTagName('compuesto')
        for compound in compounds:
            name = compound.getElementsByTagName('nombre')[0].firstChild.data
            elements = compound.getElementsByTagName('elemento')
            print(name)
            for element in elements:
                element = element.firstChild.data
                print('  ',element)
            print()

# read = Read()
# read.readFile('entrada.xml')
# read.getElements()
# read.getMachines()
# read.getCompounds()