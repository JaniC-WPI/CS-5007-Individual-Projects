from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def getRoot(self):
        return self.__root

    def setRoot(self, node):
        self.__root = node

    def insertNode(self, val):
        node = Node(val)
        if self.getRoot() is None:
            self.setRoot(node)
        else:
            self.__insertNode(val, self.getRoot())

    def __insertNode(self, val, node): # Have you seen "==", why?
        if val < node.getVal() and node.getLeft() is not None:
            self.__insertNode(val, node.getLeft())
        elif val < node.getVal() and node.getLeft() is None:
            node.setLeft(Node(val, parent=node))
        elif val > node.getVal() and node.getRight() is not None:
            self.__insertNode(val, node.getRight())
        elif val > node.getVal() and node.getRight() is None:
            node.setRight(Node(val, parent=node))
        else:
            print("The same node is trying to be inserted.")

    def searchNode(self, val):
        # Base Cases: root is null or key is present at root
        if (self.getRoot() is None or self.getRoot().getVal() == val):
            return self.getRoot()

            # Key is greater than root's key
        elif val < self.getRoot().getVal():
            return self.__searchNode(val, self.getRoot().getLeft())

            # Key is smaller than root's key
        else:
            return self.__searchNode(val, self.getRoot().getRight())

    def __searchNode(self, val, node):
        if val == node.getVal():
            return node
        elif (val < node.getVal() and node.getLeft() is not None):
            return self.__searchNode(val, node.getLeft())
        elif (val > node.getVal() and node.getRight() is not None):
            return self.__searchNode(val, node.getRight())
        else:
            return "No Such Node."

    def printTree(self):
        if self.getRoot() is not None:
            self.__printTree(self.getRoot())
        else:
            print("The tree is empty.")

    def __printTree(self, node):
        if node is not None:
            self.__printTree(node.getLeft())
            print(str(node.getVal()) + " ")
            self.__printTree(node.getRight())

    def deleteTree(self):
        self.setRoot(None)

    def getTreeSize(self):
        if self.getRoot() is None:
            return 0
        else:
            return self.__getTreeSize(self.getRoot())

    def __getTreeSize(self, node):
        if node.getLeft() is None and node.getRight() is None:
            return 1
        elif node.getLeft() is None and node.getRight() is not None:
            return 1 + self.__getTreeSize((node.getRight()))
        elif node.getLeft() is not None and node.getRight() is None:
            return 1 + self.__getTreeSize((node.getLeft()))
        else:
            return 1 + self.__getTreeSize((node.getLeft())) + self.__getTreeSize((node.getRight()))

    def getLeftMostData(self):
        if self.getRoot() is None:
            return "No Left Most Data"
        else:
            return self.__getLeftMostData(self.getRoot())

    def __getLeftMostData(self, node):
        if node.getLeft() is None:
            return node.getVal()
        else:
            return self.__getLeftMostData(node.getLeft())

    def getRightMostData(self):
        if self.getRoot() is None:
            return "No Right Most Data"
        else:
            return self.__getRightMostData(self.getRoot())

    def __getRightMostData(self, node):
        if node.getRight() is None:
            return node.getVal()
        else:
            return self.__getRightMostData(node.getRight())

    def printLeafNode(self):
        res = ""

        if self.getRoot() is None:
            res += "No Leaf Nodes"
        else:
            res += self.__printLeafNode(self.getRoot()) + " "

        return res

    def __printLeafNode(self, node):
        if node.getLeft() is None and node.getRight() is None:
            return str(node.getVal())
        elif node.getLeft() is not None and node.getRight() is None:
            return self.__printLeafNode(node.getLeft())
        elif node.getLeft() is None and node.getRight() is not None:
            return self.__printLeafNode(node.getRight())
        else:
            return self.__printLeafNode(node.getLeft()) + " " + self.__printLeafNode(node.getRight())

    def preorderTrav(self):
        res = ""

        if self.getRoot() is None:
            res += "The tree is empty."
        else:
            res += self.__preorderTrav(self.getRoot())
        return res

    def __preorderTrav(self, node):
        res = ""
        if node is not None:
            res += str(node.getVal()) + " "
            return res + self.__preorderTrav(node.getLeft()) + self.__preorderTrav(node.getRight())
        else:
            return res

    def inorderTrav(self):
        res = ""

        if self.getRoot() is None:
            res += "The tree is empty."
        else:
            res += self.__inorderTrav(self.getRoot())
        return res

    def __inorderTrav(self, node):
        res = ""

        if node.getLeft() is not None:
            res += self.__inorderTrav(node.getLeft())

        res += str(node.getVal()) + " "

        if node.getRight() is not None:
            res += self.__inorderTrav(node.getRight())
        return res

    def postorderTrav(self):
        res = ""

        if self.getRoot() is None:
            res += "The tree is empty."
        else:
            res += self.__postorderTrav(self.getRoot())
        return res

    def __postorderTrav(self, node):
        res = ""

        if node.getLeft() is not None:
            res += self.__postorderTrav(node.getLeft())

        if node.getRight() is not None:
            res += self.__postorderTrav(node.getRight())

        res += str(node.getVal()) + " "
        return res

    def levelorderTrav(self):
        list = []
        res = ""

        if self.getRoot() is None:
            return "The tree is empty."
        else:
            list.append(self.getRoot())
            self.__levelorderTrav(list, self.getRoot())

        for i in list:
            res += str(i.getVal()) + " "

        return res

    def __levelorderTrav(self, list, node):
        if node.getLeft() is not None:
            list.append(node.getLeft())

        if node.getRight() is not None:
            list.append(node.getRight())

        if node.getLeft() is not None:
            self.__levelorderTrav(list, node.getLeft())

        if node.getRight() is not None:
            self.__levelorderTrav(list, node.getRight())

    def countLeaves(self):
        # Check if the tree is empty
        if self.getRoot() is None:
            return 0
        else:
            # Call recursive function to look for the leaf nodes
            return self.__countLeaves(self.getRoot())

    def __countLeaves(self, node):
        # Recursive function to traverse the tree and count leaf nodes
        if node.getLeft() is None and node.getRight() is None:
            # Return 1 when there are no children nodes (is a leaf)
            return 1
        elif node.getLeft() is not None and node.getRight() is None:
            return self.__countLeaves(node.getLeft())
        elif node.getLeft() is None and node.getRight() is not None:
            return self.__countLeaves(node.getRight())
        else:
            return self.__countLeaves(node.getLeft()) + self.__countLeaves(node.getRight())

    def countNonLeaves(self):
        # Check if the tree is empty
        if self.getRoot() is None:
            return 0
        else:
            # Call recursive function to look for the non-leaf nodes
            return self.__countNonLeaves(self.getRoot())

    def __countNonLeaves(self, node):
        # Recursive function to traverse the tree and count nonn-leaf nodes
        if node.getLeft() is None and node.getRight() is None:
            # Return 0 when there are no children nodes (is a leaf)
            return 0

        # Return 1 plus other non-leaf nodes when there is at least one children node
        elif node.getLeft() is not None and node.getRight() is None:
            return 1 + self.__countNonLeaves(node.getLeft())
        elif node.getLeft() is None and node.getRight() is not None:
            return 1 + self.__countNonLeaves(node.getRight())
        else:
            return 1 + self.__countNonLeaves(node.getLeft()) + self.__countNonLeaves(node.getRight())

    def printParentNode(self):
        node_list = []
        # Check if the tree is empty
        if self.getRoot() is None:
            print("The tree is empty.")
        else:
            # Traverse the tree by level
            node_list.append(self.getRoot())

            # Loop while there are nodes to process
            while len(node_list) > 0:
                node = node_list.pop(0)

                # Check if the node has a parent
                if node.getParent() is None:
                    print(node.getVal(), " is a root node.")
                else:
                    print(node.getParent().getVal(), " is the parent of ", node.getVal())

                # Append child nodes to the list to process
                if node.getLeft() is not None:
                    node_list.append(node.getLeft())
                if node.getRight() is not None:
                    node_list.append(node.getRight())

