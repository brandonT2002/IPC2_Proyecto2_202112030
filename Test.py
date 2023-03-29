from Elements.LinkedListElements import LinkedListElements
from Elements.Element import Element
from Machines.LinkedListMachines import LinkedListMachines
from Machines.Machine import Machine
from Machines.LinkedListElementsPin import LinkedListElementsPin
from Compounds.LinkedListCompounds import LinkedListCompounds
from Compounds.LinkedListElementsComp import LinkedListElementsComp

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
llElements.iterated()

# agregar elementos a los pines
machine = Machine()
pin1 = LinkedListElementsPin()
pin1.insert(llElements.validateStatement('Li'))
pin1.insert(llElements.validateStatement('He'))
pin1.insert(llElements.validateStatement('N'))

pin2 = LinkedListElementsPin()
pin2.insert(llElements.validateStatement('C'))
pin2.insert(llElements.validateStatement('B'))
pin2.insert(llElements.validateStatement('H'))

machine.insert(pin1)
machine.insert(pin2)

print('\nMaquinas')
llMachines.insert('maquina1','2','6',machine)
llMachines.iterated()

# agregar elementos al compuesto
comp1 = LinkedListElementsComp()
comp1.insert('Li')
comp1.insert('Li')
comp1.insert('Be')
comp1.insert('He')
comp1.insert('Be')
comp1.insert('Li')

print('\nCompuestos')
llCompounds.insert('compuesto1',comp1)
llCompounds.iterated()