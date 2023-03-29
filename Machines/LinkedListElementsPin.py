from Machines.ElementPinNode import ElementNode

class LinkedListElementsPin:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    # movimientos
    def moveRight(self) -> bool:
        if self.current.next:
            self.current = self.current.next
            return True
        return False

    def moveLeft(self) -> bool:
        if self.current.prev:
            self.current = self.current.prev
            return True
        return False

    def getCurrent(self) -> ElementNode:
        return self.current

    def insert(self,element):
        if self.first:
            self.last.next = ElementNode(self.index,element)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = ElementNode(self.index,element)
        self.last = self.first
        self.index += 1
        self.current : ElementNode = self.first

    def iterated(self):
        current = self.first
        while current:
            print('Elemento:',current.element.symbol)
            current = current.next

    def get(self,index) -> ElementNode:
        current = self.first
        while current:
            if current.index == index:
                return current
            current = current.next
        return None

    def size(self):
        return self.index
    
    def __str__(self):
        current = self.first
        cadena = ''
        while current:
            cadena += f'{current.index} Elemento: {current.element.symbol}'
            current = current.next
            if current: cadena += '\n'
        return cadena