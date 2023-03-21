from Machines.ElementPinNode import ElementNode

class LinkedListsElementPin:
    def __init__(self):
        self.first = None
        self.last = None

    def insertElement(self,element):
        if self.first:
            self.last.next = ElementNode(element)
            self.last.prev = self.last
            self.last = self.last.next
            return
        self.first = ElementNode(element)
        self.last = self.first

    def iteratedList(self):
        current = self.first
        while current:
            print('Elemento:',current.element)
            current = current.next