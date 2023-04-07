class ElementCompNode:
    def __init__(self,index,element):
        self.index = index
        self.element = element
        self.next = None
        self.prev = None

    def getCSV(self):
        return f'{self.element}'