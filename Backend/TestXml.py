from Read import Read
from Elements.LinkedListElements import LinkedListElements
from Machines.LinkedListMachines import LinkedListMachines
from Compounds.LinkedListCompounds import LinkedListCompounds

content = '''
<?xml version="1.0"?>
<CON-FIG>
    <listaElementos>
        <elemento>
            <numeroAtomico>1</numeroAtomico>
            <simbolo>H</simbolo>
            <nombreElemento>Hidrógeno</nombreElemento>
        </elemento>
        <elemento>
            <numeroAtomico>2</numeroAtomico>
            <simbolo>He</simbolo>
            <nombreElemento>Helio</nombreElemento>
        </elemento>
        <elemento>
            <numeroAtomico>3</numeroAtomico>
            <simbolo>Li</simbolo>
            <nombreElemento>Litio</nombreElemento>
        </elemento>
        <elemento>
            <numeroAtomico>4</numeroAtomico>
            <simbolo>Be</simbolo>
            <nombreElemento>Berilio</nombreElemento>
        </elemento>
        <elemento>
            <numeroAtomico>5</numeroAtomico>
            <simbolo>B</simbolo>
            <nombreElemento>Boro</nombreElemento>
        </elemento>
        <elemento>
            <numeroAtomico>6</numeroAtomico>
            <simbolo>C</simbolo>
            <nombreElemento>Carbono</nombreElemento>
        </elemento>
        <elemento>
            <numeroAtomico>7</numeroAtomico>
            <simbolo>N</simbolo>
            <nombreElemento>Nitrógeno</nombreElemento>
        </elemento>
    </listaElementos>
    <listaMaquinas>
        <Maquina>
            <nombre>Maquina 01</nombre>
            <numeroPines>2</numeroPines>
            <numeroElementos>3</numeroElementos>
            <pin>
                <elementos>
                    <elemento>Li</elemento>
                    <elemento>He</elemento>
                    <elemento>N</elemento>
                </elementos>
            </pin>
            <pin>
                <elementos>
                    <elemento>C</elemento>
                    <elemento>Be</elemento>
                    <elemento>H</elemento>
                </elementos>
            </pin>
        </Maquina>
        <Maquina>
            <nombre>Maquina del tiempo</nombre>
            <numeroPines>2</numeroPines>
            <numeroElementos>3</numeroElementos>
            <pin>
                <elementos>
                    <elemento>Li</elemento>
                    <elemento>He</elemento>
                    <elemento>N</elemento>
                </elementos>
            </pin>
            <pin>
                <elementos>
                    <elemento>C</elemento>
                    <elemento>Be</elemento>
                    <elemento>H</elemento>
                </elementos>
            </pin>
        </Maquina>
    </listaMaquinas>
    <listaCompuestos>
        <compuesto>
            <nombre>Compuesto 01</nombre>
            <elementos>
                <elemento>Li</elemento>
                <elemento>Li</elemento>
                <elemento>Be</elemento>
                <elemento>He</elemento>
                <elemento>Be</elemento>
                <elemento>Li</elemento>
            </elementos>
        </compuesto>
    </listaCompuestos>
</CON-FIG>
'''

llElements = LinkedListElements()
llMachines = LinkedListMachines()
llCompounds = LinkedListCompounds()

read = Read()
read.readFile(content)

# print('\nElementos')
# llElements : LinkedListElements = read.getElements(llElements)
# llElements.iterated()

# print('\nMaquinas')
# llMachines : LinkedListMachines = read.getMachines(llElements,llMachines)
# llMachines.iterated()

# print('\nCompuestos')
# llCompounds : LinkedListCompounds = read.getCompounds(llCompounds)
# llCompounds.iterated()

# print('\nDot')
# llMachines.getDot(0)