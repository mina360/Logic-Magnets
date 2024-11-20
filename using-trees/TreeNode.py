class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def addChild(self, child_node):
        self.children.append(child_node)

    def findNode(self, value):
        if self.value == value:
            return self
        for child in self.children:
            result = child.findNode(value)
            if result:
                return result
        return None