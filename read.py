from xml.dom import minidom

class Read:
    def readFile(self,path):
        file = minidom.parse(path)
        listelements = file.getElementsByTagName('listaElementos')[0]
        elements = listelements.getElementsByTagName('elemento')

        print('\nElementos')
        for element in elements:
            nAtom = element.getElementsByTagName('numeroAtomico')[0].firstChild.data
            symbol = element.getElementsByTagName('simbolo')[0].firstChild.data
            name = element.getElementsByTagName('nombreElemento')[0].firstChild.data
            print(nAtom,symbol,name)

        print('\nMaquinas')
        machines = file.getElementsByTagName('Maquina')
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

        print('Compuestos')
        compounds = file.getElementsByTagName('compuesto')
        for compound in compounds:
            name = compound.getElementsByTagName('nombre')[0].firstChild.data
            elements = compound.getElementsByTagName('elemento')
            print(name)
            for element in elements:
                element = element.firstChild.data
                print('  ',element)
            print()

Read().readFile('entrada.xml')