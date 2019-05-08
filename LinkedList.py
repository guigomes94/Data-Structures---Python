from No import Node

class LinkedList:

    def __init__(self): #construtor da lista encadeada
        self.first = None #primeiro dado
        self.last = None
        self.size = 0 #controle do tamanho

    def add(self, value, index): #método para adicionar

        if index >= 0:
            no = Node(value) #criar novo nó

            if self.empty():
                self.first = no
                self.last = no

            else:
                if index == 0: #inserir no inicio
                    no.setNext(self.first)
                    self.first = no

                elif index >= self.size: #inserir no final
                    self.last.setNext(no)
                    self.last = no

                else:
                    aux_no = self.first #inserir no meio
                    cur_no = self.first.getNext()
                    aux_index = 1

                    while cur_no is not None: #percorrendo a lista

                        if aux_index == index:
                            no.setNext(cur_no)
                            aux_no.setNext(no)
                            break

                        aux_no = cur_no
                        cur_no = cur_no.getNext()
                        aux_index += 1


            self.size += 1

    def remove(self, index): #removendo dado

        if not self.empty() and index >= 0 and index < self.size:
            flag_remove = False #flag de remoção

            if self.first.getNext() is None:
                self.first = None #possui apenas 1 elemento
                flag_remove = True

            elif index == 0:
                self.first = self.first.getNext() #remove do inicio, mas tem + de 1 elemento
                flag_remove = True

            else:
                aux_no = self.first #remover em qualquer lugar
                cur_no = self.first.getNext()
                cur_index = 1

                while cur_no is not None:

                    if index == cur_index:
                        aux_no.setNext(cur_no.getNext())
                        cur_no.setNext(None)
                        flag_remove = True
                        break

                    aux_no = cur_no
                    cur_no = cur_no.getNext()
                    self.last = cur_no.getNext()
                    cur_index += 1

            if flag_remove:
                self.size -= 1

    def empty(self):
        if self.first is None:
            return True
        return False

    def length(self):
        return self.size

    def search(self, data):
        current = self.first
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            print(f"'{data}' NOT FOUND")
        return current

    def getFirst(self):
        current = self.first
        return current.getData()

    def getLast(self):
        current = self.last
        return current.getData()

    def show_all(self):

        cur_no = self.first

        while cur_no is not None:
            print(cur_no.getData(), end='')
            cur_no = cur_no.getNext()
        print()
