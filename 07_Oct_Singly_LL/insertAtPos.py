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
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node
    
    def printList(self):
        if(self.head == None):
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                print(temp.data,end=" -> ")
                temp = temp.next
            print("None")
    
    def countList(self):
        

ob1 = SinglyLL()
ob1.insertAtEnd(8)
ob1.printList()
ob1.insertAtBegin(1)
ob1.printList()

for x in [10,20,30,40]:
    ob1.insertAtEnd(x)
ob1.printList()
        