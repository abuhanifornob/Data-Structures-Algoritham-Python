
class Node:  # Node Section
    def __init__(self,value):
        self.prev=None
        self.next=None
        self.value=value

class Double_link_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def add_value(self,value): # new Value Add
        node=Node(value)
        if self.tail is None:
            self.tail=node
            self.head=node
            self.size+=1
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.size+=1
    def add_frist(self,value):
        node=Node(value)
        if self.head is not None:
            self.head.prev=node
            node.next=self.head
            self.head=node
            self.size+=1

    def __reomve_node(self, node):
        if node.prev is None:
            self.head=node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail=node.prev
        else:
            node.next.prev = node.prev
        self.size-=1

    def reome_frist(self):
        if self.head is not None:
            self.__reomve_node(self.head)
    def remove_last(self):
        if self.tail is not None:
            self.__reomve_node(self.tail)


    def remove(self,value):
        node=self.head
        while node is not None:
            if node.value==value:
                self.__reomve_node(node)
                break
            node=node.next
    def search(self,value):
        node=self.head
        while node is not None:
            if node.value == value:
                print(f"The nuber is : {value}")
                break
            node=node.next


    def __str__(self): #  print Function
        value=[]
        node=self.head
        while node is not None:
            value.append(node.value)
            node=node.next
        return f"[{' , '.join(str(val) for val in value)}]"




link_list=Double_link_list()
link_list.add_value(2)
link_list.add_value(4)
link_list.add_value(10)
link_list.add_value(4)
link_list.add_value(4)
link_list.add_value(7)
link_list.add_value(6)
print(link_list)
print(link_list.size)
link_list.remove_last()
print(link_list)
print(link_list.size)
link_list.reome_frist()
link_list.add_frist(100)
print(link_list)
print(link_list)
link_list.search(10)
