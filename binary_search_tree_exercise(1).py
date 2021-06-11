class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,child):

        if child< self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left=BinaryTreeNode(child)
        if child> self.data:
            if self.right:
                self.right.add_child(child)
            else:
                self.right=BinaryTreeNode(child)

    def in_order_traversel(self):
        element=[]

        if self.left:
            element+=self.left.in_order_traversel()

        element.append(self.data)

        if self.right:
            element+= self.right.in_order_traversel()
        return element

    def pre_order_traversel(self):
        element=[]

        element.append(self.data)

        if self.left:
            element+=self.left.pre_order_traversel()

        if self.right:
            element+=self.right.pre_order_traversel()

        return element

    def post_order_traversel(self):

        element=[]
        if self.left:
            element+=self.left.post_ordr_traversel()
        if self.right:
            element+=self.right.post_order_traversel()

        element.append(self.data)

        return element

    def search(self,data):
        if self.data==data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data> self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def sum(self):
        sum=0

        for i in self.in_order_traversel():
            sum+=i
        return sum
    def min_number(self):
         return self.in_order_traversel()[0]
    def max_number(self):
        return self.in_order_traversel()[-1]

    # Another Way Min & Max number Find....................

    def find_min_number(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min_number()

    def find_max_number(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max_number()
    def delete(self,val):
        if val< self.data:
            if self.left:
                self.left=self.left.delete(val)

        elif val> self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val=self.right.find_min_number()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self







def build_tree(element):
    root=BinaryTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root


if __name__=="__main__":
    element=[17,4,1,20,9,23,18,34]
    dft=build_tree(element)
    print("In Ordr Tree Traversel Tree",dft.in_order_traversel())
    print("Pre Order Traversel Tree", dft.pre_order_traversel())
    print(dft.sum())
    print(dft.min_number())
    print("max_number is: ",dft.find_max_number())
    dft.delete(9)
    print("after 9 Delete",dft.in_order_traversel())

