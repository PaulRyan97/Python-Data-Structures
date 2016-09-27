import random

class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode

class List:
    def __init__(self):
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(None, self.head, None)
        self.head.next = self.tail
        self.size = 0
        self.cursor = self.head

    def __str__(self):
        """ Display contents of Doubly Linked List as a string.

            Default method, that lists elements from first to last.
        """
        outstr = "-"
        node = self.head.next
        while node != self.tail:
            outstr = outstr + str(node.element) + "-"
            node = node.next
        return outstr

    def str_first_at_front(self):
        """ Display contents of Linked List as string from first to last. """
        return str(self)
    
    def str_first_at_end(self):
        """ Display contents of Linked List as string from last to first. """
        outstr = "-"
        node = self.head.next
        while node != self.tail:
            outstr = "-" + str(node.element) + outstr
            node = node.next
        return outstr
        

    def add_between(self, item, nodebefore, nodeafter):
        node = DLLNode(item, nodebefore, nodeafter)
        nodebefore.next = node
        nodeafter.prev = node
        self.size = self.size + 1

    def add(self, pos, item):
        i = 0
        node = self.head
        while i != pos:
            node = node.next
            i += 1
        self.add_between(item, node, node.next)
        
           
    def add_first(self, element):
        self.add_between(element, self.head, self.head.next)

    def add_last(self, element):
        self.add_between(element, self.tail.prev, self.tail)

    def add_current(self,item):
        node = self.cursor
        self.add_between( item, node, node.next)
        

    def get(self,pos):
        i = 0
        node = self.head
        while i != pos:
            node = node.next
            i += 1
        return node

    def get_pos(self, item):
        pos = 0
        node = self.head
        while item != node:
            node = node.next
            pos += 1
        return pos
        
    def get_current(self):
        cursorpos = self.cursor
        
        return cursorpos.element
     
    def get_first(self):
        return self.head.next.element

    def get_last(self):
        return self.tail.prev.element

    def replace(self,pos,item):
        node = self.get(pos)
        node.element = item
        
    def replace_first(self,item):
        node = self.head.next
        node.element = item

    def replace_last(self,item):
        node = self.tail.prev
        node.element = item
        

    def replace_current(self,item):
        node = self.cursor
        node.element = item

    def remove_pos(self, pos):
        node = self.get(pos)
        return self.remove_node(node)
        

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size = self.size - 1
        item = node.element
        node.element = None   #cleaning up, so that Python can save space
        node.next = None
        node.prev = None
        return item

    def remove_first(self):
        if self.size == 0:
            return None
        return self.remove_node(self.head.next)
        #need the if statement, since an empty list has
        #self.head.next == self.tail, which we don't want to remove

    def remove_last(self):
        if self.size == 0:
            return None
        return self.remove_node(self.tail.prev)
        #need the if statement, since an empty list has
        #self.tail.prev == self.head, which we don't want to remove

    def remove_current(self):
        return self.remove_node(self.cursor)

    def next(self):
        self.cursor = self.cursor.next

    def prev(self):
        self.cursor = self.cursor.prev

    def move_to_first(self):
        self.cursor = self.head.next

    def move_to_last(self):
        self.cursor = self.tail.prev

    def move_to(self,pos):
        self.cursor = self.get(pos)

    def has_next(self):
        if self.cursor != self.tail.prev:
            return True
        else:
            return False

    def find(self, item):
        pos = 0
        node = self.head
        while pos < self.length():
            if node.element == item:
                return pos
            else:
                node = node.next
                pos += 1
                
        return -1
            
    def clear(self):
        for e in range(0, self.length()):
            node = self.head.next
            nexnode = node.next
            self.remove_node(node)
            node = nexnode

    def length(self):            #report the number of elements
        return self.size

    def is_empty(self):          #report True if no elements
        return self.length() == 0

def test_list():
    inputlist = ['b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k']
    mylist = List()
    print('Empty list created:', mylist, 'with size:', mylist.length())
    for i in range(len(inputlist)):
        mylist.add_last(inputlist[i])
    mylist.add_first('a')
    mylist.add_last('l')
    mylist.add(6,'g')
    print("Is G here yet?", mylist )
    print('List filled:', mylist, 'with size:', mylist.length())
    print('First element [get_first()]:', mylist.get_first())
    print('Last element [get_last()]:', mylist.get_last())
    print('Element at index 7:', mylist.get(7))
    print('Removed first:', mylist.remove_first(),
          ', leaving list:', mylist)
    print('Removed last:', mylist.remove_last(),
          ', leaving list:', mylist)
    print('Removed node at position 5:', mylist.remove_pos(5),
          ', leaving list:', mylist)
    mylist.replace(7, 'w')
    print(mylist)
    print('Replace index 7 with -w-, leaving list:', mylist)
    mylist.replace_first('x')
    print('Replace first with -x-, leaving list:', mylist)
    mylist.replace_last('z')
    print('Replace last with -z-, leaving list:', mylist)
    print('Cursor at (should be None):', mylist.get_current())
    mylist.move_to_first()
    print('Move cursor to front, cursor at:', mylist.get_current())
    mylist.next()
    mylist.next()
    print('Cursor moved on 2 places:', mylist.get_current())
    mylist.replace_current('t')
    print('Replace current with -t-, leaving list:', mylist)
    mylist.remove_current()
    print('removed that item:', mylist, 'with cursor now at:', mylist.get_current())
    mylist.move_to_last()
    print('Cursor moved to end:', mylist.get_current())
    mylist.move_to(4)
    print('Cursor moved to position 4:', mylist.get_current())
    mylist.prev()
    mylist.prev()
    print('Cursor moved back 2 places:', mylist.get_current())
    mylist.add_current('y')
    print('Added -y- there:', mylist, 'with cursor now at:', mylist.get_current())
    print('Now printing the list using the cursor')
    mylist.move_to_first()
    outstr = '-'
    item = mylist.get_current()
    outstr = outstr + item + '-'
    while mylist.has_next():
        mylist.next()
        item = mylist.get_current()
        outstr = outstr + item + '-'
    print(outstr)
    print('-g- is in position:', mylist.find('g'))
    print('-w- is in position:', mylist.find('w'))
    mylist.clear()
    print('Clearing list:', mylist, ', now of size', mylist.length())
    print(mylist)
    print('-g- is in position:', mylist.find('g'))

def test_linkedlist():
    mylist = DLinkedList()
    mylist.add_first('b')
    mylist.add_last('c')
    mylist.add_first('a')
    mylist.add_last('d')
    mylist.add_last('e')
    print('mylist =', mylist)
    print('length =', mylist.length())
    print('first =', mylist.get_first())
    print('last = ', mylist.get_last())
    print('first (removed) =', mylist.remove_first())
    print('mylist now =', mylist)
    print('length =', mylist.length())
    mylist.remove_first()
    mylist.remove_first()
    mylist.remove_last()
    mylist.remove_last()
    print('mylist (empty?) =', mylist)
    print('length =', mylist.length())
    print('first (None?) =', mylist.get_first())
    print('last (None?) =', mylist.get_last())
    print('first removed (None?) =', mylist.remove_first())
    mylist.add_last('f')
    print('mylist (f) =', mylist)
    print('length =', mylist.length())



class Contractor:
    def __init__(self, idnum):
        self.idnum = idnum
        self.hours = 0
        
    def __str__(self):
        return '(' + str(self.idnum) + ',' + str(self.hours) + ')'

    def __eq__(self, contractor):
        if contractor == None:
            return False
        if self.idnum == contractor.idnum:
            return True
        return False

    def __ne__(self, contractor):
        return not self == contractor

class MgtSystem:

    def list_str(self, Contractors):
        Contractors.__str__()


    def lowest_cont(self, Contractors ):
        pos = 0
        lowestid  = None
        lowest = None
        node = Contractors.head.next
        while pos < Contractors.length():
            if lowest == None:
                lowestid = str(node.element.idnum)
                lowest = node.element.hours
            elif node.element.hours < lowest:
                lowestid = str(node.element.idnum)
                lowest = node.element.hours
            else:
                node = node.next
                pos += 1

        print('Contractor No.%s has the lowest number of hours.' % (lowestid))
                
    def contract_pos(self, item, Contractors):
        pos = 0
        node = Contractors.head.next
        while item != node.element:
            node = node.next
            pos += 1
        
        print('Contractor No.%s is in position "%s"' % ( item.idnum, pos ))

        
    def add_contractor(self, idnum, Contractors):
        Contractors.add_last(idnum)
        

    def remove_contractor(self, item, Contractors):
        pos = Contractors.find(item)
        Contractors.remove_pos(pos)

        
    def update_hours(self,cont,time):
        cont.hours += time


def test_mgt():
    Test = MgtSystem()
    Contractors = List()
    inputlist = [Contractor(1), Contractor(2), Contractor(3)]
    print('Empty list created:', Contractors , 'with size:', Contractors.length())
    for i in range(len(inputlist)):
        Contractors.add_last(inputlist[i])
    print(Contractors)
    
    

    Test.add_contractor(Contractor(123),Contractors)
    Test.add_contractor(Contractor(124), Contractors)
    Test.add_contractor(Contractor(125), Contractors)
    Test.add_contractor(Contractor(126), Contractors)
    Test.add_contractor(Contractor(127), Contractors)

    print('Adding Contractors',Contractors)

    Test.list_str(Contractors)

    pos = 0
    node = Contractors.head.next
    while pos < Contractors.length():
        Test.update_hours(node.element, random.randint(1, 20) )
        pos += 1
        node = node.next

    print('Assigning Jobs', Contractors)
        

    Test.lowest_cont(Contractors)

    Test.contract_pos(Contractor(124), Contractors)

    print('Removing Contractor No.126')
    Test.remove_contractor(Contractor(126), Contractors)
    print('Removing Contractor No.123')
    Test.remove_contractor(Contractor(123), Contractors)
    print('Removing Contractor No.121')
    Test.remove_contractor(Contractor(3), Contractors)

    Test.contract_pos(Contractor(124), Contractors)

    Test.add_contractor(Contractor(404),Contractors)
    Test.add_contractor(Contractor(401), Contractors)
    Test.add_contractor(Contractor(500), Contractors)

    print('Adding Contractors',Contractors)

    pos = 0
    node = Contractors.head.next
    while pos < Contractors.length():
        Test.update_hours(node.element, random.randint(1, 20) )
        pos += 1
        node = node.next

    print('Assigning Jobs', Contractors)
        
    
    
    print(Contractors)
    

    

    
