from Machines.PinNode import PinNode

class Machine:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,listElements):
        if self.first:
            self.last.next = PinNode(self.index,listElements)
            self.last.next.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = PinNode(self.index,listElements)
        self.last = self.first
        self.index += 1

    def iterated(self):
        current = self.first
        while current:
            print(current)
            current = current.next

    def getPin(self,index):
        current = self.first
        while current:
            if current.index == index:
                return current
            current = current.next
        return None

    def size(self):
        return self.index
    
    def sizeElements(self):
        return self.first.listElements.index

    def reset(self):
        current = self.first
        while current:
            current.listElements.resetMove()
            current = current.next

    def clone(self):
        newMachine = Machine()
        newMachine.index = self.index
        current = self.first
        newMachine.index = 0
        while current:
            if newMachine.first:
                newMachine.last.next = PinNode(newMachine.index,current.listElements.clone())
                newMachine.last.next.prev = newMachine.last
                newMachine.last = newMachine.last.next
                newMachine.index += 1
            else:
                newMachine.first = PinNode(newMachine.index,current.listElements.clone())
                newMachine.last = newMachine.first
                newMachine.index += 1
            current = current.next
        return newMachine

    #Graphviz
    def generatedDot(self):
        dot = 'digraph maquina {\nnode1 [shape=none, margin=0, label=\n<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="5">\n'

        current = self.first
        while current:
            dot += '<tr>\n'
            dot += f'<td BGCOLOR="gray" width="60" height="30">Pin {current.index + 1}</td>\n'

            currentE = current.listElements.first
            while currentE:
                dot += f'<td BGCOLOR="{currentE.element.color}" width="100" height="30">{currentE.element.atomcNum}<br align="left"/>{currentE.element.symbol}<br/>{currentE.element.name}</td>\n'
                currentE = currentE.next
            dot += '</tr>\n'
            current = current.next

        dot += '</TABLE>>\n'
        dot += '];\n'
        dot += '}'
        # print(dot)

        # with open('Backend/Img/imgMachine.txt','w',encoding='utf-8') as report:
        #     report.write(dot)

        # os.system('dot -Tjpg Backend/Img/imgMachine.txt -o Backend/Img/imgMachine.jpg')
        # webbrowser.open('Backend\Img\imgMachine.jpg')

        return dot

    def getStep(self,stepN,pinY,elmX,colors):
        dot = f'node{stepN} [shape=none, margin=0, label=\n<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="5">\n'
        title = f'Segundo {stepN}' if stepN > 0 else 'Estado Inicial'
        dot += f'<tr>\n<td border="0" colspan="{self.sizeElements() + 1}" align="left">{title}</td>\n</tr>'
        current = self.first
        while current:
            dot += '<tr>\n'
            color = colors.get(current.index if current.index < colors.size() else current.index % colors.size())
            dot += f'<td BGCOLOR="{color}" width="60" height="30">Pin {current.index + 1}</td>\n'
            if current.index == pinY:
                dot += f'{current.listElements.getDot(color,elmX)}'
            else:
                dot += f'{current.listElements.getDot(color)}'
            dot += '</tr>\n'
            current = current.next

        dot += '</TABLE>>\n'
        dot += '];\n'
        return dot

    def __str__(self):
        current = self.first
        stringG = ''
        while current:
            stringG += f'{current}'
            current = current.next
            if current: stringG += '\n'
        return stringG