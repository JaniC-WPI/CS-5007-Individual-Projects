from BinarySearchTree import BinarySearchTree

# Function to create a binary tree and ask for node values
def createBinaryTree():

    # Create binary search tree object
    tree = BinarySearchTree()

    # Variable to keep track if there are more nodes to add to the tree
    more_nodes = 'yes'

    # Loop until there are no more nodes to be added
    while more_nodes == 'yes':
        node_value = int(input('Please input a node value: '))

        # Insert value into tree
        tree.insertNode(node_value)

        # Ask to the user if there is another node to be added
        more_nodes = input('Do you want to add another node? [Yes/No]: ')
        # This helps since the user can type yes or no in upper or lower case
        more_nodes = more_nodes.lower()

        # Validate more_nodes answer
        while (more_nodes != 'yes') and (more_nodes != 'no'):
            more_nodes = input('Do you want to add another node? [Yes/No]: ')
            more_nodes = more_nodes.lower()

    return tree

# Function to print the content of a tree
def printBinaryTree(tree):
    print()
    # Print the parent node with all the nodes
    tree.printParentNode()

    # Print the the number of leaf and non-leaf nodes
    print('\nThe number of leaves in this tree is ', tree.countLeaves())
    print('\nThe number of non-leaves in this tree is ', tree.countNonLeaves())
    print()

def main():
    # Variable to keep track if there are more trees to be created
    cont = 'yes'

    # Loop until there are no more trees to be created
    while cont == 'yes':

        # Calling function to create and fill a tree
        tree = createBinaryTree()

        # Calling function to print the content of created tree
        printBinaryTree(tree)

        # Ask to the user if there is any tree remaining
        cont = input('Is there another tree to be created? [Yes/No]: ')
        # This helps since the user can type yes or no in upper or lower case
        cont = cont.lower()

        # Validate cont answer
        while (cont != 'yes') and (cont != 'no'):
            cont = input('Is there another tree to be created? [Yes/No]: ')
            cont = cont.lower()

    print('\nThank You for Using My Application')

if __name__ == "__main__":
    main()
