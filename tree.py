class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_label(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spech=" "*self.get_label()*5
        prefix=spech +"|---" if self.parent else ""
        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def build_product_tree():
    root=TreeNode('Electronics')
    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Lenevo"))
    asus=(TreeNode("Asus"))
    asus.add_child(TreeNode("Apple"))

    cellphone=TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Sumsung"))
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Vivo"))

    tv=TreeNode("TV")
    tv.add_child(TreeNode("Walton"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))
    laptop.add_child(asus)
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root

if __name__=="__main__":
    root=build_product_tree()
    root.print_tree()