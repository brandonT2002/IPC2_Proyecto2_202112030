from Machines.PinNode import PinNode
import os
import webbrowser

class Machine:
    def __init__(self):
        self.first = None
        self.last = None
        self.index = 0

    def insert(self,listElements):
        if self.first:
            self.last.next = PinNode(self.index,listElements)
            self.last.prev = self.last
            self.last = self.last.next
            self.index += 1
            return
        self.first = PinNode(self.index,listElements)
        self.last = self.first
        self.index += 1

    def iterated(self):
        current = self.first
        while current:
            print('Pin:',current.index)
            current.listElements.iterated()
            current = current.next

    def getPin(self,index):
        current = self.first
        while current:
            if current.index == index:
                return current
            current = current.next

    def size(self):
        return self.index
    
    def sizeElements(self):
        return self.first.index
    
    #Graphviz
    def getDot(self):
        dot = 'digraph maquina {\nnode1 [shape=none, margin=0, label=\n<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="5">\n'

        current = self.first
        while current:
            dot += '<tr>\n'
            dot += f'<td BGCOLOR="gray" width="60" height="30">Pin {current.index}</td>\n'

            currentE = current.listElements.first
            while currentE:
                dot += f'<td BGCOLOR="{currentE.element.color}" width="100" height="30">{currentE.element.atomcNum}<br align="left"/>{currentE.element.symbol}<br/>{currentE.element.name}</td>\n'
                currentE = currentE.next
            dot += '</tr>\n'
            current = current.next

        dot += '</TABLE>>\n'
        dot += '];\n'
        dot += '}'
        #print(dot)

        with open('Img/imgMachine.txt','w',encoding='utf-8') as report:
            report.write(dot)

        os.system('dot -Tjpg Img/imgMachine.txt -o Img/imgMachine.jpg')
        webbrowser.open('Img\imgMachine.jpg')