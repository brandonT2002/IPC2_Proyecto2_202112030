from ElementNode import ElementNode

class LinkedListElement:
    def __init__(self):
        self.first = None
        self.last = None

    def insertElement(self,element):
        if self.first:
            self.last.next = ElementNode(element)
            self.last.prev = self.last
            self.last = self.last.next
        self.first = ElementNode(element)
        self.last = self.first

    def existElement(self,atomicNum,symbol,name):
        current = self.first
        while current:
            if current.element.atomcNum == atomicNum and current.element.symbol == symbol and current.element.name == name:
                return True
            current = current.next
        return False

    def iteratedList(self):
        current = self.first
        while current:
            print(f'No. Atómico {current.element.atomcNum}',f'Simbolo: {current.element.symbol}',f'Nombre: {current.element.name}')
            current = current.next