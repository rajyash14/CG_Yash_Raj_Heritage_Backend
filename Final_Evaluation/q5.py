class Node:
    def __init__(self, a):
        self.val = a
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, a):
        if not self.root:
            self.root = Node(a)
        else:
            self._insert(self.root, a)

    def _insert(self, a, b):
        if b < a.val:
            if a.left is None:
                a.left = Node(b)
            else:
                self._insert(a.left, b)
        else:
            if a.right is None:
                a.right = Node(b)
            else:
                self._insert(a.right, b)

    def search(self, a, b):
        if not a:
            return False
        if a.val == b:
            return True
        if b < a.val:
            return self.search(a.left, b)
        return self.search(a.right, b)

    def delete(self, a, b):
        if not a:
            return a
        if b < a.val:
            a.left = self.delete(a.left, b)
        elif b > a.val:
            a.right = self.delete(a.right, b)
        else:
            if not a.left:
                return a.right
            elif not a.right:
                return a.left
            
            c = self.get_min(a.right)
            a.val = c.val
            a.right = self.delete(a.right, c.val)
        return a

    def get_min(self, a):
        b = a
        while b.left:
            b = b.left
        return b

    def inorder(self, a):
        if a:
            self.inorder(a.left)
            print(a.val, end=" ")
            self.inorder(a.right)

    def preorder(self, a):
        if a:
            print(a.val, end=" ")
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.val, end=" ")


a = BST()
for b in [50, 30, 20, 40, 70, 60, 80, 35]:
    a.insert(b)

print(a.search(a.root, 40))
print(a.search(a.root, 90))

print("Inorder before:")
a.inorder(a.root)
print("\nPreorder before:")
a.preorder(a.root)
print("\nPostorder before:")
a.postorder(a.root)
print()

a.root = a.delete(a.root, 20)
a.root = a.delete(a.root, 30)
a.root = a.delete(a.root, 50)

print("Inorder after:")
a.inorder(a.root)
print("\nPreorder after:")
a.preorder(a.root)
print("\nPostorder after:")
a.postorder(a.root)
print()