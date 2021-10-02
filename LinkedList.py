# -------------- Node class ---------------- #
class Node:
      def __init__(self, data):
            self.data =  data
            self.next =  None
       
# ------------- LinkedList class --------------- #
class LinkedList:
     def __init__(self):
           self.head = None
     
     # this method is to iterate to linkedlist  
     def __iter__(self):
            node = self.head
            while (node is not None):
                  yield node
                  node = node.next
     
     # this method is to visualize does node point to next node 
     def show(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        print(" -> ".join(nodes))
        print(nodes)
        
     # this method is use for inserting a node at first or at beginning
     def insertAtFirst(self, node):
           node.next = self.head
           self.head = node
           
    # this method is use for inserting a node at last or at the end
     def insertAtLast(self, node):
           if self.head == None:
                 self.head == node 
                 return
           
           for current_node in self:pass #  here we are traversing to the end 
           current_node.next = node # and makes the current_node as last node
     
     # this method insert node between two nodes 
     def insertAfter(self, target_data , new_node):
           if self.head == None:
                 raise Exception("Empty list")
           
           for node in self:
                 if node.data == target_data:
                       new_node.next = node.next
                       node.next = new_node
                       return
                  
           raise Exception ("Target node not found !!")

     def removeNode(self, target_data):
           if self.head == None:
                 raise Exception ("Empty list")
           
           if self.head.data == target_data:# here we are setting next node as head
                 self.head == self.head.next
                 return
           
           one_before = self.head
           
           for node in self: # here we are traversing until we find target node
                 if node.data == target_data: 
                       one_before.next = node.next # here we are pointin before target node to the next target node
                       return
                 
                 one_before = node
           
           raise Exception ("Target node not found !!")
      
     # reverse the linkedlist           
     def reverse(self):
           prev = None
           current = self.head
           while(current is not None):
                 next = current.next 
                 current.next = prev
                 prev = current
                 current = next
           self.head = prev
           
# ============== Calling all methods ================ # 
firstNode = Node("B")
secondNode = Node("C")
thirdNode = Node("D")

ll = LinkedList()

ll.head = firstNode
firstNode.next = secondNode
secondNode.next = thirdNode


ll.insertAtFirst(Node("A"))
ll.insertAtLast(Node("E"))
#ll.insertAfter("E", Node("F"))

#ll.removeNode("c")

ll.show()

ll.reverse()

ll.show()
