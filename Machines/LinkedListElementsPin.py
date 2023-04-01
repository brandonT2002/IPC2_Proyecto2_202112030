from Machines.ElementPinNode import ElementNode
from Elements.Element import Element
class LinkedListElementsPin:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0
        self.current = None
        self.moved = False

    # movimientos
    def moveRight(self) -> bool:
        if self.current.next:
            self.current = self.current.next
            self.moved = True
            return True
        return False

    def moveLeft(self) -> bool:
        if self.current.prev:
            self.current = self.current.prev
            self.moved = True
            return True
        return False

    def getCurrent(self) -> ElementNode:
        return self.current

    def resetMove(self):
        self.moved = False

    def insert(self,element : Element):
        if self.first:
            self.last.next = ElementNode(self.index,element)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = ElementNode(self.index,element)
        self.last = self.first
        self.index += 1

    def startPin(self):
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

    def clone(self):
        newList = LinkedListElementsPin()
        current = self.first
        while current:
            newList.insert(current.element.clone())
            current = current.next
        newList.current = self.current
        return newList

    def getDot(self,color,elmX = -1):
        current = self.first
        dot = ''
        while current:
            color_ = color
            border = ''
            if self.current:
                if current.index > self.current.index:
                    color_ = 'white'
                elif elmX != -1 and current.index == elmX:
                    color_ = 'gray'
                    border = ' border="3"'
            else:
                color_ = 'white'
            dot += f'<td BGCOLOR="{color_}" width="100" height="30"{border}>{current.element.symbol}</td>\n'
            current = current.next
        return dot

    def size(self):
        return self.index
    
    def __str__(self):
        current = self.first
        cadena = ''
        while current:
            cadena += '{:<4}'.format(current.element.symbol)
            current = current.next
        return cadena