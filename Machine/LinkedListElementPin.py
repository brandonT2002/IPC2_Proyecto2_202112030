from Machine.ElementPinNode import ElementNode

class LinkedListElementPin:
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

    def validateStatement(self,atomicNum):
        current = self.first
        while current:
            if current.element.atomcNum == atomicNum:
                return current.element.atomcNum
            current = current.next