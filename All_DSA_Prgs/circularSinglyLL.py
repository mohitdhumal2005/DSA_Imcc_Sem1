# Circluar Singly LinkedList:
# 1. Appending the Node at First Position and End
# 2. Print The List

class Node: #Creating of Node Class
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL: #SinglyLL Class Created
    
    def __init__(self):  #init() method for head node
        self.head = None
    
    # def insertAtBegin(self,data):  #inserting the node from the start
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node
    
    # def insertAtEnd(self, data):    #insertion of data from the end i.e. appending
    #     new_node = Node(data)
    #     if(self.head == None):
    #         self.head = new_node
    #     else:
    #         temp = self.head
    #         while(temp.next!=None):
    #             temp = temp.next
    #         temp.next = new_node
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:       # Inserting Node at First Position
            self.head = new_node
            new_node.next = self.head
        else:                       # Inserting the Nodes at the end
            temp = self.head
            while (temp.next!=self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            
    def insertAtPos(self,data,pos):
        new_node = Node(data)
        if pos<1 or pos>self.countLL()+1:
            print("Invalid Position!")
        elif pos == 1:
            if self.head == None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while(temp.next!=self.head):
                    temp = temp.next
                new_node.next = self.head
                self.head = new_node
                temp.next = new_node
        else:
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def printList(self):            #Printing the SLL
        if (self.head == None):
            print("List is Empty!")
        else:
            temp = self.head
            while(True):
                print(temp.data,end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
            print("Back To Head")
    
    def countLL(self):
        count = 0
        if self.head != None:
            temp = self.head
            while True:
                count = count + 1
                temp = temp.next
                if temp == self.head:
                    break
        return count

    def delFirstPosition(self):                 # delete the first node
        if self.head == None:                       # if there is no node
            print("List is empty!") 
        elif self.head.next == self.head:           # if there is only one node
            self.head = None
        else:                                       # if there are multiple nodes
            temp = self.head
            while(temp.next!=self.head):
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
            
    def delLastNode(self):          # Delete the Last node
        if self.head == None:           # if there is no node
            print("List is empty!")
        elif self.head.next == self.head:       # if there is only one node
            self.head = None
        else:                               # if there are multiple nodes
            temp = self.head
            while(temp.next.next!=self.head):
                temp = temp.next
            temp.next = self.head
        

    def deleteByPos(self,pos):
        if pos<1 or pos>self.countLL():         #if pos is less than 1 or greater than no. of nodes
            print("Invalid Position to Delete!")
        elif pos == 1:                          # if pos is 1 
            if self.head.next == self.head:             # if there is only one node and want to delete first node
                self.head = None
            else:                                       # if there are multiple nodes and want to delete first node
                temp = self.head
                while(temp.next!=self.head):
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
        else:                           # to delete the node at any position
            temp = self.head
            for i in range(pos-2):
                temp = temp.next
            temp.next = temp.next.next
                

ob1 = SinglyLL()
# ob1.insertAtEnd(20)
# ob1.printList()
# ob1.insertAtBegin(10)
# ob1.printList()

# for x in [30,40,50]:
#     ob1.insertAtEnd(x)
# ob1.printList()

# print("Total No. of Node: ",ob1.countLL())

ob1.append(10)
ob1.printList()
ob1.append(20)
ob1.printList()
for x in [30,40,50]:
    ob1.append(x)
ob1.printList()

ob1.insertAtPos(5,1)
ob1.printList()

ob1.insertAtPos(5,0)
ob1.insertAtPos(15,3)
ob1.printList()

ob1.insertAtPos(100,8)
ob1.printList()


ob1.deleteByPos(1)
ob1.printList()

ob1.deleteByPos(4)
ob1.printList()

ob1.deleteByPos(7)
ob1.printList()




