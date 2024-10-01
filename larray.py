import ctypes

class Meralist:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__makeArray(self.size)
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.size == self.n:
            #resize
            self.__resize(self.size*2)

        #append 
        self.A[self.n] = item
        self.n =self.n + 1
    
    def __resize(self, capacity):
        # create a new array with new capacity
        b = self.__makeArray(capacity)
        self.size = capacity
        # copy item from old array to list array 
        for i in range(self.n):
            b[i]= self.A[i]
        #resign
        self.A = b
    
    def __makeArray(self, capacity):
        return (capacity*ctypes.py_object)()
    
#    This is display fuction 

    def __str__(self):
        resutl = ''
        for i in range(self.n):
            resutl = resutl + str(self.A[i]) + ","
        return "[" + resutl[:-1] + "]"
    
    def __getitem__(self,item):
        if 0 <= item <self.n:
            return self.A[item]
        else:
            return "demag thikane pr hai y  nahiiii"
    
    def pop(self):
        if self.n == 0:
            return "empty list"
        else :
            self.n -=1
            return self.A[self.n-1]
    
    def clear(self):
        self.n = 0
        self.size = 1
    
    def index(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'item not found'
    
    # insert function
    def insert(self, index,item):
        # check list have empty or full
        if self.n == self.size:  
            #resize
            self.__resize(self.size*2)
        
        # sifting item 
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i-1]
        self.A[index] = item
        self.n +=1

    def __delitem__ (self,index):
        if 0 <= index <= self.n:
            for i in range(index,self.n-1):
                self.A[i]=self.A[i+1]
            self.n -=1
        
            
l = Meralist()

l.append('piyush')
l.append(63)
l.append(2)
l.append(1)

# print(l.index(7))
l.insert(0,"Mr. ")
del l[0]

print(l)

