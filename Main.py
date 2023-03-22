from Read.Read import Read
from Elements.LinkedListElements import LinkedListElements
from Machines.LinkedListMachines import LinkedListMachines
from Compounds.LinkedListCompounds import LinkedListCompounds

llElements = LinkedListElements()
llMachines = LinkedListMachines()
llCompounds = LinkedListCompounds()

read = Read()
read.readFile('entrada.xml')
print('\nElementos')
llElements : LinkedListElements = read.getElements(llElements)
llElements.iterated()

print('\nMaquinas')
llMachines : LinkedListMachines = read.getMachines(llMachines)
llMachines.iterated()

print('\nCompuestos')
llCompounds : LinkedListCompounds = read.getCompounds(llCompounds)
llCompounds.iterated()