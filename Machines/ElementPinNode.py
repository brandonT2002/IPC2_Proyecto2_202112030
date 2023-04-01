from Elements.Element import Element
class ElementNode:
    def __init__(self,index,element : Element):
        self.index = index
        self.element : Element = element
        self.next = None
        self.prev = None