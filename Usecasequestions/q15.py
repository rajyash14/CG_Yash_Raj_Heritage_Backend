class StudentNode:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.left = None
        self.right = None

class StudentDatabase:
    def __init__(self):
        self.root = None
        
    def insert(self, root, roll_no, name):
        if root == None:
            return StudentNode(roll_no, name)
        if roll_no < root.roll_no:
            root.left = self.insert(root.left, roll_no, name)
        elif roll_no > root.roll_no:
            root.right = self.insert(root.right, roll_no, name)
        return root
        
    def search(self, root, roll_no):
        if root == None:
            return "Student not found"
        if root.roll_no == roll_no:
            return root.name
        if roll_no < root.roll_no:
            return self.search(root.left, roll_no)
        return self.search(root.right, roll_no)

db = StudentDatabase()
root = None
root = db.insert(root, 101, "Alice")
root = db.insert(root, 105, "Bob")
root = db.insert(root, 102, "Charlie")

print(db.search(root, 105))
print(db.search(root, 103))