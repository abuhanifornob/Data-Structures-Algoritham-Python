from collections import deque

class Queue:
    def __init__(self):
        self.container=deque()
    def enqueue(self,item):
        self.container.appendleft(item)
    def size(self):
        return len(self.container)
    def dequeue(self):
        return self.container.pop()

class S_Queue:
    def __init__(self,size):
        self.items=[0]*size
        self.max_size=size
        self.head,self.tail,self.size=0,0,0

    def s_enqueue(self,item):
        self.items[self.tail]=item
        self.tail=(self.tail+1)%self.max_size
        self.size+=1
    def s_dqueue(self):
        item=self.items[self.head]
        self.head=(self.head+1) % self.max_size
        self.size-=1

        return item

    def is_full(self):
        if self.size==self.max_size:
            return True
        return False
    def is_empty(self):
        if self.size==0:
            return True
        return False




if __name__ == "__main__":
    q=Queue()
    q.enqueue('hanif')
    print(q.container)
