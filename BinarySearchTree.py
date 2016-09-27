class BSTNode:
    """ An internal node in a (doubly linked) binary search tree. """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

            The string will be created by an in-order traversal.
        """
        outstr = ''
        if self._leftchild:
            outstr = outstr + str(self._leftchild)
        outstr = outstr + ' ' + str(self._element)
        if self._rightchild:
            outstr = outstr + str(self._rightchild)
        return outstr

    def _stats(self):
        """ Return a string of the basic stats for the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))    
  
    def search(self, item):
        """ Return the first subtree containing item, or None. """
        if item == self._element:
            print(self.__str__())
        elif item < self._element:
            if self._leftchild != None:
                if item == self._leftchild:
                    print(self._leftchild)
                else:
                    self._leftchild.search(item)
        elif item > self._element:
            if self._rightchild != None:
                if item == self._rightchild:
                    print(self._rightchild)
                else:
                    self._rightchild.search(item)
        else:
            return None

    def add(self, item):
        """ Add item to the tree, maintaining BST properties.
            Note: if item is already in the tree, this does nothing.
        """
        if item < self._element:
            if self._leftchild == None:
                self._leftchild = BSTNode(item)
                self._leftchild._parent = self
            else:
                self._leftchild.add(item)

        elif item > self._element:
            if self._rightchild == None:
                self._rightchild = BSTNode(item)
                self._rightchild._parent = self
            else:
                self._rightchild.add(item)

        
    def findmin(self):
        """ Return the minimal element below this node. """
        while self._leftchild != None:
            return self._leftchild.findmin()
        print( self._element )
    
    def _findminnode(self):
        """ Return the BSTNode with the minimal element below this node. """
        while self._leftchild != None:
            return self._leftchild.findmin()
        return self

    def findmax(self):
        """ Return the maximal element below this node. """
        while self._rightchild != None:
            return self._rightchild.findmax()
        print( self._element )

    def _findmaxnode(self):
        """ Return the BSTNode with the maximal element below this node. """
        while self._rightchild != None:
            return self._rightchild.findmax()
        return self

        
    def height(self):
        """ Return the height of this node.

            Note that with the recursive definition of the tree the height
            of the node is the same as the depth of the tree rooted at this
            node.
        """
        if self == None:
            return 0
        elif self._leftchild == None and self._rightchild == None:
            return 0
        else:
            if self._leftchild == None:
                return 1 + (self._rightchild.height())
            elif self._rightchild == None:
                return 1 + (self._leftchild.height())
            else:
                return 1 + max(self._leftchild.height(), self._rightchild.height())

    def size(self):
        """ Return the size of this subtree.

            The size is the number of nodes (or elements) in the tree.
        """
        count = 0
        if self != None:
            if self._leftchild != None:
                count += 1 + self._leftchild.size()
            if self._rightchild != None:
                count += 1 +self._rightchild.size()
        return count
##        if self == None:
##            return 0
##        elif self._leftchild == None and self._rightchild == None:
##            return 0
##        else:
##            if self._leftchild == None:
##                return 1 + (self._rightchild.size())
##            elif self._rightchild == None:
##                return 1 + (self._leftchild.size())
##            else:
##                return 1 + self._leftchild.size() , 1 + self._rightchild.size()


    def leaf(self):
        """ Return True if this node has no children. """
        if self._leftchild == None and self._rightchild == None:
            return True
        else:
            return False

    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if self.leaf():
            return False
        elif self._leftchild == None or self._rightchild == None:
            return True
        else:
            return False

    def full(self):
        """ Return true if this node has two children. """
        if not self.leaf() and not self.semileaf():
            return True
        return False

    def internal(self):
        """ Return True if this node has at least one child. """
        if not self.leaf():
            return True
        return False

    def remove(self, item):
        """ Remove and return item from the tree rooted at this node.

            Maintains the BST properties.
        """
        if item < self._element:
            if self._leftchild._element == item:
                self = self._leftchild
            else:
                self._leftchild.remove(item)
        elif item > self._element:
            if self._rightchild._element == item:
                self = self._rightchild
            else:
                self._rightchild.remove(item)
                
        if self._parent:
            parent = self._parent
            
            if self.full():
                if self._element > parent._element:
                    parent._rightchild = self._leftchild
                    self._leftchild._parent = parent
                    parent._rightchild._rightchild = self._rightchild
                    self._rightchild._parent = parent._rightchild
                else:
                    parent._leftchild = self._leftchild
                    self._leftchild._parent = parent
                    parent._leftchild._rightchild = self._rightchild
                    self._rightchild._parent = parent._leftchild
                   
                self = None
                
            elif self.semileaf():
                if self._leftchild:
                    if self._leftchild._element > parent._element:
                        parent._rightchild = self._leftchild
                        self._leftchild._parent = parent
                    else:
                        parent._leftchild = self._leftchild
                        self._leftchild._parent = parent
                else:
                    if self._rightchild._element > parent._element:
                        parent._rightchild = self._rightchild
                        self._rightchild._parent = parent
                    else:
                        parent._leftchild = self._rightchild
                        self._rightchild._parent = parent
                self = None
                    
            elif self.leaf():
                if self._element > parent._element:
                    parent._rightchild = None
                else:
                    parent._leftchild = None
        else:
            if self._leftchild:
                self._leftchild._parent = None
                if self._rightchild:
                    self._rightchild._parent = self._leftchild
                self = self._leftchild

    
            else:
                self = self._rightchild
                self._rigthchild._parent = None

            self =  None
            
                    


        

    def _remove_node(self):
        """ (Private) Remove this BSTBode from its tree.

            Maintains the BST properties.
        """
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element
        
        if item < self._element:
            if self._leftchild._element == item:
                self = self._leftchild
            else:
                self._leftchild.remove(item)
        elif item > self._element:
            if self._rightchild._element == item:
                self = self._rightchild
            else:
                self._rightchild.remove(item)
                
        if self._parent:
            parent = self._parent
            
            if self.full():
                if self._element > parent._element:
                    parent._rightchild = self._leftchild
                    self._leftchild._parent = parent
                    parent._rightchild._rightchild = self._rightchild
                    self._rightchild._parent = parent._rightchild
                else:
                    parent._leftchild = self._leftchild
                    self._leftchild._parent = parent
                    parent._leftchild._rightchild = self._rightchild
                    self._rightchild._parent = parent._leftchild
                   
                self = None
                
            elif self.semileaf():
                if self._leftchild:
                    if self._leftchild._element > parent._element:
                        parent._rightchild = self._leftchild
                        self._leftchild._parent = parent
                    else:
                        parent._leftchild = self._leftchild
                        self._leftchild._parent = parent
                else:
                    if self._rightchild._element > parent._element:
                        parent._rightchild = self._rightchild
                        self._rightchild._parent = parent
                    else:
                        parent._leftchild = self._rightchild
                        self._rightchild._parent = parent
                self = None
                    
            elif self.leaf():
                if self._element > parent._element:
                    parent._rightchild = None
                else:
                    parent._leftchild = None
        else:
            if self._leftchild:
                self._leftchild._parent = None
                if self._rightchild:
                    self._rightchild._parent = self._leftchild
                self = self._leftchild

    
            else:
                self = self._rightchild
                self._rigthchild._parent = None

            self =  None
                    
                

                
            


    def _pullup(self, node):
        """ Pull up the child tree rooteed at node into this BSTNode. """
        #method body goes here.

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        outstr = str(self._element) + '(' + str(self.height()) + ')['
        if self._leftchild:
            outstr = outstr + str(self._leftchild._element) + ' '
        else:
            outstr = outstr + '* '
        if self._rightchild:
            outstr = outstr + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '*]'
        if self._parent:
            outstr = outstr + ' -- ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- *'
        print(outstr)
        if self._leftchild:
            self._leftchild._print_structure()
        if self._rightchild:
            self._rightchild._print_structure()

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild.isthisapropertree() == False:
                ok = False
        if self._rightchild:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild.isthisapropertree() == False:
                ok = False          
        if self._parent:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode('mushroom')
        node._print_structure()
        print('adding green bean')
        node.add('green bean')
        node._print_structure()
        node.add('carrot')
        node.add('leek')
        node._print_structure()
        print('adding radish')
        node.add('radish')
        node._print_structure()
        print('adding pea')
        node.add('pea')
        node._print_structure()
        print('adding pepper')
        node.add('pepper')
        node._print_structure()
        print('adding parsnip')
        node.add('parsnip')
        node._print_structure()
        node.search('mushroom')
        node.search('pea')
        print(node.size())
        node.findmin()
        node.findmax()
        node._findminnode()
        node._findmaxnode()
        node.remove('mushroom')
        node._print_structure()
        node.remove('radish')
        node._print_structure()
        return node
            
    def _test():
        node = BSTNode(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 0)
        node.add(0)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 0)
        node.remove(0)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 6)
        node.add(6)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 1)
        node.remove(1)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 2)
        node.add(2)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 4)
        node.add(4)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 3)
        node.add(3)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 5)
        node.add(5)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 2)
        node.remove(2)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 4)
        node.remove(4)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 3)
        node.remove(3)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 5)
        node.remove(5)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 12)
        node.add(12)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 8)
        node.add(8)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 9)
        node.add(9)
        print('Ordered:', node)
        node._print_structure()
        print('adding', 7)
        node.add(7)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 12)
        node.remove(12)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 8)
        node.remove(8)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 9)
        node.remove(9)
        print('Ordered:', node)
        node._print_structure()
        print('removing', 7)
        node.remove(7)
        print('Ordered:', node)
        node._print_structure()

import re

def wordbst(filename):
    """ Return a bst containing the words in file 'filename'. """
    for e in filename:
        file = open(e, 'r')  #open the file
        fulltext = file.read()         #read it all into one big string
        stripped = re.sub('[^a-zA-Z\s]+', '', fulltext)  #remove non-letters or -spaces
        wordlist = stripped.split() #split the string on white space into words in a list
        print(e,len(wordlist), 'words in total')
        bst = BSTNode(wordlist[0])
        for word in wordlist:
            bst.add(word)
    
        print("Size" ,bst.size())
        print("Height" ,bst.height())
        bst.search("blood")
        bst.search("screaming")
        bst.search("science")
        print("**********END************")
    return bst

        
