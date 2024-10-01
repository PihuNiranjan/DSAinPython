"""
operation in stack
peek -> return top element on stack
push -> insertion element on stack 
pop  -> delete element on stack
isempty-> return t if stack is empty else false

"""

# IMPLEMENTATION OF STACK USING LINKED LIST

"""

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
    
    def isempty(self):
        return self.top == None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        string = ""
        while temp!=None:
            string += str(temp.data) + "->"
            temp = temp.next
        print(string[:-2])

    def peek(self):
        if(self.isempty()):
            return "stack Underflow"
        return self.top.data
    
    def pop(self):
        if(self.isempty()):
            return "stack is underflow"
        else:
            data = self.peek()
            self.top = self.top.next
            return data


    def reverse_string(self, string):
        for i in string:
            self.push(i)
        temp = self.top
        res = ""
        while temp!=None:
            res+=self.pop()
            temp = temp.next
        return res


st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
# st.push(4)

# st.traverse()  
# print("peek element is : ",st.peek())

# print("element  after pop operation : ")
# st.pop()
# st.traverse()


print(st.reverse_string("piyush"))
"""





# implementation of stack using list 

"""
class stack():
    def __init__(self):
        self.a =[]
    
    def push(self,value):
        return self.a.append(value)
    
    def poop(self):
        return self.a.pop()

    def peek(self):
        return self.a[-1]
    
    def isempty(self):
        return len(self.a) ==0

    def traverse(self):
        for i in self.a:
            print(i,end=" ")
    
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.traverse()

s.poop()
print()
s.traverse()
print("\n",s.peek())
print(s.isempty())

"""