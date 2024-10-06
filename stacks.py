## create a stack
## What do you mean by stack?

#A Stack is a linear data structure that holds a linear, o
# rdered sequence of elements. It is an abstract data type. A Stack works on the LIFO proc
# ss (Last In First Out), i.e., the element that was inserted last will be removed first.
# LIFO
## aplications : when we press back button  in browser or undo and redo  operations in word processor

class  Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[] ## create empty list

    def push(self,item):
        self.items.append(item) ## add element

    def pop(self):
        return self.items.pop() ##delete last element
    
    def peek(self):
        return self.items[len(self.items)-1] ## peek last element

    def size(self):
        return len(self.items) ## size of list stack

s = Stack()

print(s.items)
s.push("A")
s.push("B")
print(s.items)
print(s.size())
print(s.peek())
print(s.pop())
print(s.items)