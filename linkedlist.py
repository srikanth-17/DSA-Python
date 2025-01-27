class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insertbeg(self,data):
        self.head=Node(data,self.head)

    def insertend(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        x=self.head
        while x.next:
            x=x.next
        x.next=Node(data,None)
    def insertmany(self,datalist):
        self.head=None
        for i in datalist:
            self.insertend(i)
            
    def size(self):
        if self.head is None:
            print("empty")
        x=self.head
        c=0
        while x:
            x=x.next
            c=c+1
        return c
    
    def removeind(self,ind):
        c=0
        if ind==0:
            self.head=self.head.next
            
        x=self.head
        while x:
            if c==ind-1:
                x.next=x.next.next
            x=x.next
            c+=1
    def insertat(self,index,data):
        if index<0 or index>self.size():
            raise Exception("Error")
        if index==0:
            self.head=self.insertbeg(data)
            return
        x=self.head
        c=0
        while x:
            if c==index-1:
                node=Node(data,x.next)
                x.next=node
            
            x=x.next
            c+=1
    
    def searchele(self,data):
        c=0
        x=self.head
        while x:
            if x.data==data:
                return True,c
            x=x.next
            c+=1
        return False,-1
        
    def display(self):
        if self.head!=None:
            x=self.head
            s=""
            while x:
                s+=str(x.data)+'--'
                x=x.next
        print(s)
        
           
"""ll=Linkedlist()
ll.insertbeg(20)
ll.insertbeg(25)
ll.insertbeg(555)
ll.insertend(100)
ll.display()"""
lll=Linkedlist()
lll.insertmany(["srikanth","kavitha","GURU","aathmika"])
print(lll.size())
lll.display()
lll.insertat(2,"Gururathnam")
lll.display()
found,pos=lll.searchele("GURU")
if found:
    print(f"found at {pos}")
else:
    print("not found ")
found,pos=lll.searchele("XXX")
if found:
    print(f"found at {pos}")
else:
    print("not found ")

