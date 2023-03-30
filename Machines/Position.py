class Position:
    def __init__(self,index,element,pinY,elmX):
        self.index = index
        self.element = element
        self.pinY = pinY
        self.elmX = elmX
        self.next = None
        self.prev = None