class GroupTreeNode:
    def __init__(self):
        self.group_exist = False
        self.children = {}

    def insert(self, pts):
        curr = self
        inserted = False
        for pt in pts:
            i = pt.index()
            if i not in curr.children:
                inserted = True
                node = GroupTreeNode()
                curr.children[i] = node
            else:
                node = curr.children[i]
            curr = node
        curr.group_exist = True
        return inserted
