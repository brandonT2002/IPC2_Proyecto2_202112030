from Elements.LinkedListElements import LinkedListElements
from Elements.Element import Element
from Machines.LinkedListMachines import LinkedListMachines
from Machines.Machine import Machine
from Machines.LinkedListElementsPin import LinkedListElementsPin
from Compounds.LinkedListCompounds import LinkedListCompounds
from Compounds.LinkedListElementsComp import LinkedListElementsComp
from Algorithm.Algorithm import Algorithm

llElements = LinkedListElements()
llMachines = LinkedListMachines()
llCompounds = LinkedListCompounds()

print('\nElementos')
llElements.insert(Element('1','H','Hidrógeno'))
llElements.insert(Element('2','He','Helio'))
llElements.insert(Element('3','Li','Litio'))
llElements.insert(Element('4','Be','Berilio'))
llElements.insert(Element('5','B','Boro'))
llElements.insert(Element('6','C','Carbono'))
llElements.insert(Element('7','N','Nitrógeno'))
llElements.insert(Element('8','O','Oxígeno'))
llElements.insert(Element('9','Na','Sodio'))
llElements.insert(Element('10','Cl','Cloro'))
llElements.insert(Element('11','Fe','Hierro'))
llElements.insert(Element('12','Z','Zinc'))
llElements.insert(Element('13','Au','Oro'))
llElements.iterated()

# agregar elementos a los pines
machine = Machine()
pin1 = LinkedListElementsPin()
pin1.insert(llElements.validateStatement('Li'))
pin1.insert(llElements.validateStatement('He'))
pin1.insert(llElements.validateStatement('N'))

pin2 = LinkedListElementsPin()
pin2.insert(llElements.validateStatement('C'))
pin2.insert(llElements.validateStatement('Be'))
pin2.insert(llElements.validateStatement('H'))

pin3 = LinkedListElementsPin()
pin3.insert(llElements.validateStatement('O'))
pin3.insert(llElements.validateStatement('Au'))
pin3.insert(llElements.validateStatement('Na'))

machine.insert(pin1)
machine.insert(pin2)
#machine.insert(pin3)

print('\nMaquinas')
llMachines.insert('maquina1','3','9',machine)
llMachines.iterated()
print(machine.size(),machine.sizeElements())

# agregar elementos al compuesto
comp1 = LinkedListElementsComp()
comp1.insert('H')
comp1.insert('H')
comp1.insert('Be')
comp1.insert('N')
comp1.insert('C')
comp1.insert('Li')

print('\nCompuestos')
llCompounds.insert('compuesto1',comp1)
llCompounds.iterated()
print('-----------------')

# enviando una máquina al algoritmo para formar componentes
maquina = llMachines.getMachine(0).machine
compuesto = llCompounds.getCompound(0).elements

# print(type(maquina))

# llMachines.getDot(0)
alg = Algorithm(maquina)
alg.buildElement(compuesto)