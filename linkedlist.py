class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        # empty linked list , condition of empty linked list is "self.head = None"
        self.head = None
        self.n = 0  # number of node
    
    
    # in linked list the lenght of linked list is equal to number of node 
    def __len__(self):
        return self.n
    # -----------INSERTION OPERATION----------------
    
    # insertion at begining
    def insertbegin(self,value):
        # create node 
        newnode = Node(value)
        # linking node
        newnode.next = self.head
        #  resigning head
        self.head = newnode
        # increment node by one
        self.n = self.n+1

    # insertion at end
    def insertionatend(self,value):
        newNode = Node(value) 
        if self.head ==None:
            self.head = newNode
            self.n = self.n+1
            return
        
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = newNode 
        self.n = self.n + 1

#   insertion after particular index
    def insertionAtIndex(self,value,index):
        newNode = Node(value)
        if index >self.n:
            print("Index is not found")
            return

        curr = self.head
        for i in range(1,index-1):
            curr = curr.next
        rightnode = curr.next
        curr.next = newNode
        newNode.next=rightnode 

        self.n = self.n+1

    # insertion after partucular element
    def insertafterele(self,element,data):
        newnode = Node(data)

        curr = self.head
        while curr !=None:
            if curr.data == element:
                break
            curr = curr.next
        # if element found then 
        if curr!=None:
            right = curr.next
            curr.next = newnode
            newnode.next = right
        else:
            print("element not found")
        self.n = self.n + 1


    # DELETION OPERATION

    # clear all list 
    def clear(self):
        self.head = None
        self.n = 0

    # delete head node

    def deletehead(self):
        if self.head == None:
            return "list is empty"
        data = self.head.data    
        self.head = self.head.next
        self.n = self.n -1
        return data
    
    def deletetail(self):
        if self.head == None:
            return

        curr = self.head
        # kya linked list me 1 node hai......
        if curr.next == None:
            return self.deletehead()
        while curr.next.next!=None:
            curr = curr.next
        data = curr.next.data

        curr.next = None
        self.n = self.n-1
        return data

    def deleteitem(self,item):
        curr = self.head
        # right = self.head.next
        if self.head == None:
            return "list is empty"
        if curr.data == item:
            self.deletehead()
            return self.head.data
        while curr.next!=None:
            if curr.next.data == item:
                break
            curr = curr.next
        
        # at that pont of time there is two condition that can we happen 
        # 1 item not found
        if curr.next ==None:
            return "Not found "
        else :
            data = curr.next.data 
            curr.next = curr.next.next
            self.n = self.n-1
            return data
        
    
    def deletebyindex(self,index):
        if self.n <= index:
            return "index not found in list..."
        if index == 0:
            return self.deletehead()
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        data = curr.next.data
        curr.next = curr.next.next
        self.n = self.n-1
        return data

    # SEARCHING ELEMENT
    # search by value

    def search(self,element):
        curr = self.head
        index = 0
        while curr!=None:

            if curr.data==element:
               return index
            curr = curr.next
            index +=1


    # search by index
    def searchelembyindex(self, index):
        curr = self.head
        if self.n <=index:
            return "index value out of range"
        for i in range(index):
            curr = curr.next
        return curr.data

                
    def reverse(self):
        prev = None
        curr = self.head

        while curr!=None:
            next = curr.next
            curr.next= prev
            prev = curr
            curr = next
        self.head = prev



    def __str__(self):
        curr = self.head
        result = ''
        while curr !=None:
            result = result+str(curr.data) + " "
            curr = curr.next
        return result[:-1]
    
    def change_sentence(self):
        temp = self.head
        while temp !=None:
            if temp.data == "*" or temp.data =="/":
                temp.data = " "
                temp= temp.next
                if temp.data == "*" or temp.data =="/":
                    if temp.data == "*":
                        self.deleteitem("*")
                    else:
                        self.deleteitem("/")
                    temp = temp.next
                    temp.data = temp.data.capitalize()        

            temp = temp.next





# a = ll()
# a.insertionatend(1)
# a.insertionatend(2)
# a.insertionatend(3)
# a.insertionatend(4)
# a.insertionatend(5)
# a.insertionatend(0)

# a.insertionAtIndex("piyush",3)

# a.insertafterele("p","niranjan")

# print(a)
# a.clear()
# print("lenght of our linked list ",len(a))  
# a.deletehead()
# print(a.deletetail())
# print("linked list after remove head node",a)                                       
# print("lenght of our linked list ",len(a))  

# a.deleteitem(5)
# print("linked list after deletion ",a)

# print("the postion of element 1 is ",a.search(1))
# print("the element of index 4 is ",a.searchelembyindex(4))
# a.deletebyindex(1)
# print("after removing the element of index 1 ",a)
# print("lenght of our linked list ",len(a))  

# a.reverse()

# print(a)

char = ll()
char.insertionatend("T")
char.insertionatend("h")
char.insertionatend("e")
char.insertionatend("/")
char.insertionatend("*")
char.insertionatend("s")
char.insertionatend("k")
char.insertionatend("y")
char.insertionatend("*")
char.insertionatend("i")
char.insertionatend("s")
char.insertionatend("/")
char.insertionatend("/")
char.insertionatend("b")
char.insertionatend("l")
char.insertionatend("u")
char.insertionatend("e")

print(char)

char.change_sentence()
print(char)