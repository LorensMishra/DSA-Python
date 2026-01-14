class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,x):
        self.q.append(x)
    def dequeue(self):
        if not self.q:
            return None
        return self.q.pop(0)# remove element from front
    def display(self):
        print("Queue", self.q)

