
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        space=" " * self.get_level()*3
        prefix=space+ "|-- " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Apple"))
    laptop.add_child(TreeNode("Deel"))

    cell_phone=TreeNode("Cell_Phone")
    cell_phone.add_child(TreeNode("Nokia"))
    cell_phone.add_child(TreeNode("Samsung"))
    cell_phone.add_child(TreeNode("Vivo"))

    tv=TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Walton"))

    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(tv)

    return root


if __name__=="__main__":
    tree=build_product_tree()
    tree.print_tree()



