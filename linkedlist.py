class Node:

    def __init__(self,data):
        self.data = data
        self.pointer = None

class linkedlist:
    def  __init__(self) -> None:
        self.head = None

    def add(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while (cur.pointer is not None):
                cur = cur.pointer

            cur.pointer = newnode

    def remove(self,data):
        if (self.head is not None):
            if (self.head.data is data):
                self.head = self.head.pointer
            else:
                cur = self.head
                while(cur.pointer is not None and cur.pointer.data is not data):
                    cur = cur.pointer
                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
        else:
            print(f"Linked list is empty")
        
    
    def print_node(self):
        cur = self.head
        
        while (cur is not None):
            print(cur.data,end=" ")
            cur = cur.pointer



    
    
link1 = linkedlist()
link1.add(1)
link1.add(2)
link1.add(3)
link1.add(4)
link1.print_node()
link1.remove(2)
print("")
link1.print_node()
  
