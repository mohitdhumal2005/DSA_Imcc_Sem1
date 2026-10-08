class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:
    
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node
    
    def insertAtPos(self,data,pos):
        new_node = Node(data)
        if(pos<1 or pos>self.countLL()+1):
            print("Invalid position")
        
        elif pos==1:
            new_node.next = self.head
            self.head = new_node
        
        else:
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def deleteFirst(self):
        if(self.head == None):
            print("List is Emmpty!")
        else:
            self.head = self.head.next
    
    def deleteLast(self):
        if(self.head == None):
            print("List is Empty!")
        elif(self.head.next == None):
            self.head = None
        else:
            temp = self.head
            while(temp.next.next!=None):
                temp = temp.next
            temp.next = None
    
    def deleteByPos(self,pos):
        if(pos<1 or pos>self.countLL()):
            print("Invalid Position!")
        elif (pos==1):
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            temp.next = temp.next.next
    
    def deleteByValue(self,value):
        if(self.head == None):
            print("List is Empty!")
        elif()
    
    def printList(self):
        if (self.head == None):
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                print(temp.data,end=" -> ")
                temp = temp.next
            print("None")
    
    def countLL(self):
        count = 0
        if(self.head == None):
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                count = count + 1
                temp = temp.next
            return count

ob1 = SinglyLL()
ob1.insertAtEnd(20)
ob1.printList()
ob1.insertAtBegin(10)
ob1.printList()

for x in [30,40,50]:
    ob1.insertAtEnd(x)
ob1.printList()

print("Total No. of Node: ",ob1.countLL())

ob1.insertAtPos(150,4)
ob1.printList()
print("Total No. of Node: ",ob1.countLL())

ob1.deleteFirst()
ob1.printList()
print("Total No. of Node: ",ob1.countLL())

ob1.deleteLast()
ob1.printList()
print("Total No. of Node: ",ob1.countLL())

ob1.deleteByPos(3)
ob1.printList()
print("Total No. of Node: ",ob1.countLL())

for x in [5,10,15,18,19]:
    ob1.insertAtEnd(x)
ob1.printList()
print("Total No. of Node: ",ob1.countLL())


