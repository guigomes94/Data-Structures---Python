class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, p):
        self.data = p

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next = n
