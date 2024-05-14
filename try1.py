class Node: 

    def __init__(self, data): 

        self.data = data 

        self.next = None 

  

def nextSmallerValue(head): 

    stack = [] 

    result = [] 

  

    current = head 

  

    while current is not None: 

        while stack and stack[-1].data > current.data: 

            stack[-1].data = current.data 

            stack.pop() 

  

        stack.append(current) 

        current = current.next 

  

    while stack: 

        stack[-1].data = -1 

        stack.pop() 

  

    return head 

  

# Example usage: 

def printList(head): 

    current = head 

    while current: 

        print(current.data, end=" ") 

        current = current.next 

    print() 

  

# Test case 

t = int(input()) 

for _ in range(t): 

    n = int(input()) 

    values = list(map(int, input().split())) 

  

    # Creating the linked list 

    head = Node(values[0]) 

    current = head 

    for i in range(1, n): 

        current.next = Node(values[i]) 

        current = current.next 

  

    # Calling the function to find next smaller values 

    head = nextSmallerValue(head) 

  

    # Printing the result 

    printList(head) 