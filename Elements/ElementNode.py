from Element import Element
class ElementNode:
    def __init__(self,element):
        self.element : Element = element
        self.next = None
        self.prev = None