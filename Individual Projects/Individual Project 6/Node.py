class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        # Attributes to record the value, left node, right node and parent of a node
        self.__val = val
        self.__left = left
        self.__right = right
        self.__parent = parent

    def getVal(self):
        return self.__val

    def setVal(self, newVal):
        self.__val = newVal

    def getLeft(self):
        return self.__left

    def setLeft(self, newLeft):
        self.__left = newLeft

    def getRight(self):
        return self.__right

    def setRight(self, newRight):
        self.__right = newRight

    # function to get a node's parent
    def getParent(self):
        return self.__parent

    def setParent(self, newParent):
        self.__parent = newParent