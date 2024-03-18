#code to implement doubly linked list
class Node:
    def __init__(self,data):
        self.item = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def search(self,data):
        current = self.head
        while(current):
            if(current.item == data):
                return current
            current = current.next
        return None
    
    #insert a new Node at the starting of the Doubly linked list
    def insertFirst(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    #insert a new Node inside the Doubly linked list
    def insertInside(self,current,data):
        if current == None:
            print("Node is not present in the Doubly linked list")
        newNode = Node(data)
        if current.next is not None:
            current.next.prev = newNode
        newNode.prev = current
        newNode.next = current.next
        current.next = newNode
        

    #insert a new Node at the last of the Doubly linked list
    def insertLast(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            current = self.head
            while(current.next != None):
                 current = current.next
            current.next = newNode
            newNode.prev = current
            newNode.next = None

    #deleting the first Node of the linked list
    def deleteAtFirst(self):
        if self.is_empty():
            print("List is empty!")
        elif self.head.next is None:
            self.head == None
        else:
            self.head = self.head.next
            self.head.prev = None,
    
    #deleting a Node inside the doubly linked list
    def deleteInside(self,data):
        if self.is_empty():
            print("List is empty")
        elif self.head.item == data:
            self.deleteAtFirst()
        else:
            current = self.head
            while(current != None):
                if(current.item == data):
                    if(current.next == None):
                        current.prev.next = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    return
                current = current.next            

    
    #printing the doubly linked list
    def display(self):
        current = self.head
        while(current):
            print(current.item,end=" ")
            current = current.next        



list = DLL()
list.insertLast(2)
list.insertFirst(1)
list.insertLast(3)
list.insertInside(list.search(1),4)
list.display()
print()
list.deleteInside(3)
list.display()
