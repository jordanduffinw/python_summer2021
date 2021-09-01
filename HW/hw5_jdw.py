### Major thanks to Cecilia Sui for helping me work through this
class Node:
    def __init__(self, _value = None, _next = None):
        self.value = _value
        self.next = _next
    
    def __str__(self):
        return str(self.value)

### Making LinkedList
class LinkedList:
    def __init__(self, value):
        self.value = Node(value, None)
        #self.next = Node(_next)
        
# Returning the Length
# Complexity is O(n) 
    def length(self):
        ct = 0
        curr = self.value
        while curr is not None:
            curr = curr.next
            ct += 1
        return "Length is: " + str(ct)
    
# Adding a number to the end of the list
# Complexity is O(n)
    def addNode(self, new_value):
        newnode = Node(new_value, None)
        curr = self.value
        while curr.next is not None:
            curr = curr.next
        curr.next = newnode
        
# Adding a new node and inserting it behind after_node
# Complexity is O(1)        
    def addNodeAfter(self, new_value, after_node):
        newnode = Node(new_value, None)
        newnode.next = after_node.next
        after_node.next = newnode

# Adding a new node and inserting it before before_node
# Complexity is O(n)    
    def addNodeBefore(self, new_value, before_node):
        newnode = Node(new_value, None)
        if before_node is self.value:
            newnode.next = self.value
            self.value = newnode
        else:
            curr = self.value
            while curr.next.value != before_node.value:
                curr = curr.next
            newnode.next = curr.next
            curr = newnode
            
# Removing a node from the list
# Complexity is O(n)
    def removeNode(self, node_to_remove):
        if node_to_remove is self.value:
            self.value = self.value.next
        else:
            curr = self.value
            while curr is not node_to_remove:
                curr = curr.next
            curr.next = curr.next.next
        return

# Removing nodes with a given value from the list
# Complexity is O(n)
    def removeNodesByValue(self, value):
        curr = self.value
        previous = self.value
        while curr:
            if curr.value == value:
                if curr is self.value:
                    self.value = curr.next
                else:
                    previous.next = curr.next
            else:
                previous = curr
            
            curr = curr.next
        
        return

# Reversing hte order of LinkedList
# Complexity is O(n)
    def reverse(self):
        previous = None
        curr = self.value
        while curr:
            nextnode = curr.next
            curr.next = previous
            previous = curr
            curr = nextnode
        self.value = previous
        return

# Returning the list:
# Complexity is O(n)
    def __str__(self):
        out = " "
        curr = self.value
        while curr:
            out += str(curr.value) + " - "
            curr = curr.next
        return out + "NULL"
        

                
        
# Testing: initialize with node = 1      
L = LinkedList(1)
print(L)

# Testing: add node 2 to the end
L.addNode(2)
print(L)

# Testing: print the length
print(L.length())

# Testing: add node after (putting 3 after 1 but before 2)
L.addNodeAfter(3, L.value)
print(L)

# Testing: add node before (putting 4 ahead of 1)
L.addNodeBefore(4, L.value)
print(L)

# Testing: Remove (in this case, the first node)
L.removeNode(L.value)
print(L)

# Testing: Remove node with value 2
L.removeNodesByValue(2)
print(L)

# Testing: Reverse
L.reverse()
print(L)

# And the __str__ works with every iteration of print()!
