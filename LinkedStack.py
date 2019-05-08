from No import Node

class LinkedStack:

    def __init__(self): #construtor
        self.top = None
        self.size = 0

    def add(self, value): #adicionar dado

            p = Node(value) #criar novo nó

            if self.empty():
                self.top = p

            else:
                p.setNext(self.top)
                self.top = p

            self.size += 1

    def remove(self): #removendo dado
        if not self.empty():
            self.top = self.top.getNext()
            self.size -= 1

    def empty(self):
        if self.top is None:
            return True
        return False

    def length(self):
        return self.size

    def show_top(self):
        return self.top.getData()

    def show_all(self):

        current_no = self.top

        print('Todos os elementos: ', end='')
        while current_no is not None:
            print(f'{current_no.getData()}', end=' ')
            current_no = current_no.getNext()
        print()
