class TreeNode:

    def __init__(self, key, value, right=None, left=None):
        self.key = key
        self.value = value
        self.right = right
        self.left = left
        self.height = 0


class BSTTree:

    def __init__(self):
        self.root = None
        self.nodes = 0

    def insert(self, key, value):
        node = TreeNode(key, value)  # criar novo nó

        if self.root is None:
            self.root = node
            self.nodes += 1

        else:
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node
                    # left or right?
                    if node.key < curr_node.key:
                        curr_node = curr_node.left
                    else:
                        curr_node = curr_node.right
                else:
                    if node.key < dad_node.key:
                        dad_node.left = node
                        self.nodes += 1

                    else:
                        dad_node.right = node
                        self.nodes += 1
                    break


    def search(self, curr_node, key):

        if curr_node is None:
            return "Empty"

        elif curr_node.key == key:
            return curr_node.value

        elif curr_node.key > key:
            return self.search(curr_node.left, key)

        else:
            return self.search(curr_node.right, key)

    # encontrar o sucessor para remoção do 3ª caso
    def findSucc(self, node):  # o nó que vai ser apagado
        father_suc = node
        suc = node
        curr_no = node.right  # vai para a subarvore a direita

        while curr_no is not None:  # enquanto nao chegar no Nó mais a esquerda
            father_suc = suc
            suc = curr_no
            curr_no = curr_no.left  # caminha para a esquerda

        if suc != node.right:  # se sucessor nao é o filho a direita do Nó que deverá ser eliminado
            father_suc = suc.right  # pai herda os filhos do sucessor que sempre serão a direita
            suc.right = node.right  # guardando a referencia a direita do sucessor

        return suc

    def remove(self, key):
        if self.root is None:
            return False  # empty tree

        curr_no = self.root
        father = self.root
        left_child = True
        flag_remove = False

        #Buscando...
        while curr_no.key != key:  # enquanto nao encontrou
            father = curr_no
            if key < curr_no.key:  # caminha para esquerda
                curr_no = curr_no.left
                left_child = True

            else:  # caminha para direita
                curr_no = curr_no.right
                left_child = False

            if curr_no is None:
                return False  # encontrou uma folha -> sai

        #1º caso - se folha
        if curr_no.left is None and curr_no.right is None:
            if curr_no == self.root:
                self.root = None  # se raiz
                flag_remove = True

            else: #se filho
                if left_child:
                    father.left = None
                    flag_remove = True

                else:
                    father.right = None
                    flag_remove = True


        # 2ª caso - pai de apenas um filho a esquerda
        elif curr_no.right is None:
            if curr_no == self.root:
                self.root = curr_no.left

            else:
                if left_child:
                    father.left = curr_no.left  # se for filho a esquerda do pai
                    flag_remove = True

                else:
                    father.right = curr_no.left  # se for filho a direita do pai
                    flag_remove = True

        # 2ª caso - pai de apenas um filho a direita
        elif curr_no is None:
            if curr_no == self.root:
                self.root = curr_no.right  # se raiz

            else:
                if left_child:
                    father.left = curr_no.right  # se for filho a esquerda do pai
                    flag_remove = True

                else:
                    father.right = curr_no.right  # se for  filho a direita do pai
                    flag_remove = True

        # 3º caso - pai com 2 filhos
        else:
            sucessor = self.findSucc(curr_no)
            if curr_no == self.root:
                self.root = sucessor  # se raiz

            else:

                if left_child:
                    father.left = sucessor  # se for filho a esquerda do pai

                else:
                    father.right = sucessor  # se for filho a direita do pai

            sucessor.left = curr_no.left  # acertando o ponteiro a esquerda do sucessor
            flag_remove = True
        if flag_remove is True:
            self.nodes -= 1

    def length(self):
        return self.nodes

    def deep(self, curr_node):

        if curr_node is None or (curr_node.left is None and curr_node.right is None):
            return 0

        else:
            if self.deep(curr_node.left) > self.deep(curr_node.right):
                return 1 + self.deep(curr_node.left)

            else:
                return 1 + self.deep(curr_node.right)


    def inOrder(self, current):
        if current is not None:
            self.inOrder(current.left)
            print(current.key, end=" ")
            self.inOrder(current.right)
