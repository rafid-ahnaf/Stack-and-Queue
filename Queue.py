class Queue:
    q = []
    front = 0
    rear = -1
    print("queue made")
    
    def enqueue(self,value):
        self.q = self.q + [value]
        self.rear +=1
    
    def dequeue(self):
        temp = self.q[self.front]
        self.q = self.q[self.front+1 : self.rear+1]
        self.rear -= 1
        
        return temp
    
    def peek(self):
        print(self.q[self.front])
    
    def display(self):
        print(self.q)


q1 = Queue()
q1.enqueue(20)
q1.display()
q1.enqueue(30)
q1.enqueue(60)
q1.enqueue(50)
q1.enqueue(40)
q1.display()
q1.peek()
q1.dequeue()
q1.display()
q1.peek()