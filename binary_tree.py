class Binary_Tree_Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data==self.data:
            return   # node already exit
        if data <self.data:
            #add data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_Tree_Node(data)
        else:
            #add data in the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_Tree_Node(data)

    def in_order_traversal(self):
        elements=[]
        #visit left Tree
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)  #visit Node
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements +=self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):         # Post Order Traversal .................
        elements=[]
        if self.left:
            elements +=self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements


    def search(self,val):                    #Value Search Function
        if val==self.data:
            return True

        if val< self.data:
            if self.left:
                 return self.left.search(val)
            else:
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def max_value(self):
        if self.right is None:
            return self.data

        return self.right.max_value()

    def min_value(self):
        if self.left is None:
            return self.data
        return self.left.min_value()

    def sum_calculation(self):
        left_sum=self.left.sum_calculation() if self.left else 0
        right_sum=self.right.sum_calculation() if self.right else 0
        return left_sum + self.data + right_sum

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right
            min_val=self.right.min_value()
            self.data=min_val
            self.right=self.right.delete(val)





def build_binary_tree(elements):
    print(" Building Tree with this Elements ")

    root=Binary_Tree_Node(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__=="__main__":
    number=[17,4,1,9,20,18,34,23]
    number_tree=build_binary_tree(number)

    search_val=20
    print(number_tree.search(search_val))
    print("In Order Traversal is ",number_tree.in_order_traversal())
    print("Pre Order Traversal is: ",number_tree.pre_order_traversal())
    print("post Order Traversal is: ", number_tree.post_order_traversal())
    number_tree.delete(20)
    print("Dlete 20",number_tree.post_order_traversal())
    print("max Number is: ",number_tree.max_value())
    print("Min Number is ",number_tree.min_value())
    print("Claculation sum is: ",number_tree.sum_calculation())
