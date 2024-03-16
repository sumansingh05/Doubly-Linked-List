#code of Doubly Linked List
class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
        self.prev = None
        
        
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
    
    def insertFirst(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def insertInside(self,current,data):
        if current == None:
            print("Node is not present in linked list")
        else:
            newNode = Node(data)
            newNode.next = current.next
            current.next.prev = newNode
            current.next = newNode
            newNode.prev = current


    def insertLast(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            newNode.prev = current    
            current.next = newNode
            newNode.next = None

    def deleteFirst(self):
        if self.is_empty():
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next

    def deleteInside(self,data):
        if self.is_empty():
            print("List is empty")
        elif self.head.item == data:
            self.deleteFirst()
        else:
            current = self.head
            while(current.next != None):
                if(current.next.item == data):
                    current.next.next.prev = current
                    current.next = current.next.next
                    return
                current = current.next
    

    def deleteLast(self):
        if self.is_empty():
            print("List is empty")
        elif self.head.next == None:
            self.head = None
        else:
            current = self.head
            while(current.next.next != None):
                current = current.next
           # current.next.prev = current
            current.next = None


    def display(self):
        current = self.head
        while(current):
            print(current.item,end = " ")
            current = current.next


list = DLL()
list.insertFirst(2)
list.insertFirst(1)
#list.insertInside(list.search(2),500)
list.insertLast(3)
list.insertLast(4)
list.insertLast(5)
list.display()
print()
#list.deleteInside(1)
#list.display()


    