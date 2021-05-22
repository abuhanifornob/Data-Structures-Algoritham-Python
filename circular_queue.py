class Circular_Queue:
    def __init__(self,size):
        self.item=[0]*size
        self.size,self.head,self.tail=0,0,0
        self.max_size=size

    def enqueue(self,item):
        if self.is_full():
            print("Queue Is Full")
            return
        print("Inserting -> ",item)
        self.item[self.tail]=item
        self.tail=(self.tail+1)%self.max_size
        self.size+=1

    def dqueue(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        item=self.item[self.head]
        self.head=(self.head+1)%self.max_size
        self.size-=1
        return item



    def is_full(self):
        if self.max_size==self.size:
            return True
        return False

    def is_empty(self):
        if self.head==0:
            return True
        return False
    def __str__(self):
        qlist=''
        for data in self.item:
            qlist +=str(data) +"--> "
        return qlist
if __name__=="__main__":
    my_queue=Circular_Queue(5)
    my_queue.enqueue(5)
    my_queue.enqueue(8)
    my_queue.enqueue(10)
    my_queue.enqueue(12)

    print(my_queue)

