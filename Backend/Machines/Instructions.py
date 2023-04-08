class Instruction:
    def __init__(self,index,value):
        self.index = index
        self.value = value
        self.next: Instruction = None
        self.last: Instruction = None

class Pin:
    def __init__(self,number):
        self.number = number
        self.first: Instruction = None
        self.last: Instruction = None
        self.next: Pin = None
        self.prev: Pin = None
        self.index = 0

    def insert(self,instruction):
        if self.first:
            self.last.next = Instruction(self.index,instruction)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = Instruction(self.index,instruction)
        self.last = self.first
        self.index += 1

    def getDot(self):
        dot = f'<td width="60" align="left">Pin {self.number + 1}</td>\n'
        current = self.first
        while current:
            dot += f'<td width="100" align="left">{current.value}</td>\n'
            current = current.next
        return dot

class Instructions:
    def __init__(self):
        self.first: Pin = None
        self.last: Pin = None

    def insert(self,pin,instruction):
        pin_ = self.__existPin(pin)
        if pin_:
            pin_.insert(instruction)
            return
        self.__insertNewPin(pin)
        self.last.insert(instruction)

    def getDot(self):
        dot = 'digraph instructions {\n'
        dot += 'nodeInstructions [shape=none, margin=0, label=\n<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">\n'
        current = self.first
        dot += '<tr>\n<td border="0"></td>\n'
        for i in range(current.index):
            dot += f'<td>Segundo {i + 1}</td>\n'
        dot += '</tr>\n'
        while current:
            dot += f'<tr>\n{current.getDot()}</tr>\n'
            current = current.next
        dot += '</TABLE>>\n'
        dot += '];\n}'
        return dot

    def __insertNewPin(self,pin):
        if self.first:
            self.last.next = Pin(pin)
            self.last.next.prev = self.last
            self.last = self.last.next
            return
        self.first = Pin(pin)
        self.last = self.first

    def __existPin(self,pin) -> Pin:
        current = self.first
        while current:
            if current.number == pin:
                return current
            current = current.next
        return None