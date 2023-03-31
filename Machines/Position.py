class Position:
    def __init__(self,index,element,pinY,elmX):
        self.index = index
        self.element = element
        self.pinY = pinY
        self.elmX = elmX
        self.next = None
        self.prev = None

    def __str__(self):
        return '* {}\n-fusiona: pin = {:<4} elemento = {:<4}'.format(self.element,self.pinY,self.elmX)