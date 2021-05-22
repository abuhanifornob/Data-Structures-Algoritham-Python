class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_lavel(self):
        h=self.parent
        level=0
        while h:
            level+=1
            h=h.parent
        return level
    def print(self,chose):
        if chose=="both":
            value=self.name + " ("+ self.designation +") "
        elif chose=="designation":
            value=self.designation
        else:
            value=self.name
        space= " " * self.get_lavel()*3
        prefix=space+ "|-- " if self.parent else ""
        print(prefix+ value)
        for child in self.children:
            child.print(chose)





def build_tree():
    root=TreeNode("Abu Hanif ","CEO")
    cto=TreeNode("Mozit","CTO")
    infrastructure_head = TreeNode("Santo", "Infrastructure Head")
    infrastructure_head.add_child(TreeNode("Samasu","Cloud Manager"))
    infrastructure_head.add_child(TreeNode("Surovo","App Manager"))
    app_head = TreeNode("Amir", "Applications Head")
    cto.add_child(infrastructure_head)
    cto.add_child(app_head)
    hr_head=TreeNode("Santa","HR Head")

    root.add_child(cto)
    root.add_child(hr_head)
    return root
if __name__=="__main__":
    root=build_tree()
    root.print('designation')


