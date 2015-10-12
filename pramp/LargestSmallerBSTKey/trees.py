from bintrees import AVLTree

############## MONKEY PATCH AVLTree ##############
### ------------------------------------------ ###

AVLTree.original_init = AVLTree.__init__

def init(self, thing):
    if type(thing) == list:
        mapping = {x:x for x in thing}
        self.original_init(mapping)
    else:
        self.original_init(thing)

def display(self, node=None, level=0):
    if not node: node = self._root

    if node.right:
        self.display(node.right, level + 1)
        print ('\t' * level), ('    /')

    print ('\t' * level), node.key

    if node.left:
        print ('\t' * level), ('    \\')
        self.display(node.left, level + 1)

AVLTree.__init__ = init
AVLTree.display = display

### ------------------------------------------ ###