class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None
    
class DoublyList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head

    def isEmpty(self):
        print("Empty linked list?",self.head is None)
        return self.head is None    

    def addNodeLast(self, val):  #adds a node at the end of the linked list
        current = self.head  #start at the head
        while current.next != None:   #goes to the end of the linked list
            current = current.next
        newNode = Node(val)   #creates a new node
        current.next = newNode  #linking
        newNode.prev = current  #linking
        self.tail = newNode     #new node is the tail
   
    def search_member(self,val):   #useful for insertNode function, checking whether the value is in the linked list so that there will be no Nonetype error
        current = self.head
        while current != None:
            if current.value == val:
                return True
            else:
                current = current.next
        return False
    
    def insertNode(self, val, newVal):  #inserting a new value (newVal) after a value in the linked list (val)
        if self.search_member(val):   #searches whether the element exists
            if self.tail.value == val:   #if the value is at the tail of the list, just add the newVal behind it
                self.addNodeLast(newVal)
            elif self.head.value == val:  #if the value is at the head of the list
                newNode = Node(newVal)
                newNode.next = self.head.next
                newNode.prev = self.head
                newNode.next.prev = newNode
                #self.head.next = newNode  
                newNode.prev.next = newNode  #this also works
            else:   #if the value is between head and tail
                current = self.head.next
                while current.value != val:   #finding the value
                    current = current.next
                newNode = Node(newVal)
                #same linking process as the second case
                """ original version
                newNode.next = current.next
                newNode.next.prev = newNode 
                newNode.prev = current
                current.next = newNode"""
                newNode.next = current.next
                newNode.prev = current
                newNode.next.prev = newNode
                newNode.prev.next = newNode

        else:
            raise Exception("The element", val, "is not in the list")    
    
    def removeNode(self, val):
        if self.head == self.tail:  #if there is only one element in the linked list
            while (self.head != None):  #look at this later (deletes all elements in a linked list)
                temp = self.head
                self.head = self.head.next
                temp = None   #replaces the temporary variable with None (deleting it)
        elif self.head.value == val:
            self.head = self.head.next  #the new head is the value one after head
            self.head.prev = None
        elif self.tail.value == val:
            self.tail = self.tail.prev  #the new tail is the previous value of the old tail
            self.tail.next = None 
        else:
            current = self.head.next
            while current.value != val:
                current = current.next
            current.prev.next = current.next  #skipping the removed value
            current.next.prev = current.prev

    def showReverse(self):  #traversing the linked list from the end and going backwards
        current = self.tail
        while current != None:
            print(current.value)
            current = current.prev

    def show(self):  #going forwards
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

dList = DoublyList(10)
dList.addNodeLast(20)
#dList.removeNode(10)   #TODO: NoneType object has no attribute value????
#dList.insertNode(20,"!")  #inserting the value 2 after 10
dList.addNodeLast(30)
dList.addNodeLast(40)
dList.removeNode(10)
dList.show()
dList.isEmpty()
#print("*********")
#dList.showReverse()