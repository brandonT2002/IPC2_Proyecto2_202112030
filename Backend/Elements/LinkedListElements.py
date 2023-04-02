from Elements.ElementNode import ElementNode

class LinkedListElements:
    def __init__(self):
        self.first : ElementNode = None
        self.last : ElementNode = None
        self.index = 0

    def insert(self,element):
        if self.first:
            self.last.next = ElementNode(self.index,element)
            self.last.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = ElementNode(self.index,element)
        self.last = self.first
        self.index += 1

    def existElement(self,atomicNum,symbol,name):
        current = self.first
        while current:
            if current.element.atomcNum == atomicNum and current.element.symbol == symbol and current.element.name == name:
                return True
            current = current.next
        return False

    def validateStatement(self,element):
        current = self.first
        while current:
            if current.element.symbol == element:
                return current.element
            current = current.next

    def iterated(self):
        current = self.first
        while current:
            print(f'No. Atómico {current.element.atomcNum}',f'Simbolo: {current.element.symbol}',f'Nombre: {current.element.name}')
            current = current.next