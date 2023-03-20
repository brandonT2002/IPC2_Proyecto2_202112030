from Read import Read
from Elements.LinkedListElements import LinkedListElement
llElements = LinkedListElement()

read = Read()
read.readFile('entrada.xml')
llElements : LinkedListElement = read.getElements(llElements)
llElements.iteratedList()