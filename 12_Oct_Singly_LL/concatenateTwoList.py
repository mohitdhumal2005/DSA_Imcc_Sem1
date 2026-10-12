""" This is the program specifically for Concatenating two List! """

class Node:                     #Creating a Node Class which contains data and pointer to next node
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLL:             # Creating Class SinglyLL which conatins Operations on List
    def __init__(self):
        self.head = None
        
    def createList(self,data):      # method for Appending the List
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node
            
    def printList(self):            # method for printing the list
        if self.head == None:
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                print(temp.data,end=" -> ")
                temp = temp.next
            print("None")
    
    def insertAtPos(self,data,pos):         # method for inserting a node at particular pposition
            new_node = Node(data)
            if pos<1 or pos>self.countList()+1:
                print("Invalid Position")
            elif pos==1:
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                for i in range(pos-2):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                
    
    def countList(self):                # method for counting the nodes
        count = 0
        if self.head == None:
            print("List is Empty!")
        else:
            temp = self.head
            while(temp):
                count+=1
                temp = temp.next
            return count
        
    def concatenateList(self,list2):      # Conacatenating the list2 at the end of list1
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = list2.head  
         
    
         
        
list1 = SinglyLL()

list1.createList(10)
list1.createList(20)
list1.createList(30)
list1.createList(40)
# print("Linked List After Creation: ",end="")
# list1.printList()


for i in [50,60,70,80,90]:
    list1.createList(i)
list1.printList()
# list1.insertAtPos(5,1)
# list1.insertAtPos(8,2)
# print("After Inserting Node at 1st and 2nd Position: ",end="")
# list1.printList()


list2 = SinglyLL()
for i in [100,200,300,400]:
    list2.createList(i)
list2.printList()

list1.concatenateList(list2)
list1.printList()
