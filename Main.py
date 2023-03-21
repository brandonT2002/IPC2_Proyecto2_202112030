from Read import Read
from Elements.LinkedListElements import LinkedListElements
from Machines.LinkedListElementsPin import LinkedListElementsPin
from Machines.Machine import Machine
from Machines.LinkedListMachines import LinkedListMachines

llElements = LinkedListElements()
llMachines = LinkedListMachines()

read = Read()
read.readFile('entrada.xml')
llElements : LinkedListElements = read.getElements(llElements)
llElements.iterated()

llMachines : LinkedListMachines = read.getMachines(llMachines)
llMachines.iterated()