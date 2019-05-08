from No import Node

class LinkedQueue:

    def __init__(self): #construtor
        self.top = None
        self.last = None
        self.size = 0

    def add(self, value): #método para adicionar

            p = Node(value) #criar novo nó

            if self.last is not None:
                self.last.next = p

            else:
                self.top = p

            self.last = p
            self.size += 1

    def remove(self): #removendo dado
        if not self.empty():
            self.top = self.top.next
            self.size -= 1
        else:
            print('Empty')

    def empty(self):
        if self.top is None and self.last is None:
            return True
        return False

    def length(self):
        return self.size

    def getTop(self):
        return self.top.getData()

    def getLast(self):
        return self.last.getData()

    def show_all(self):

        no = self.top

        print('Todos os elementos: ', end='')
        while no is not None:
            print(f'{no.getData()}', end=' ')
            no = no.getNext()
        print()
