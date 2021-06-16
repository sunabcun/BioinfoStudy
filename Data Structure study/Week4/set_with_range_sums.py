class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.sum = 0


class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def left_rotate(self, x):
        # R side
        y = x.right
        # Left rotate
        x.right = y.left
        # If y.left exists, set x as a parent
        if y.left != None:
            y.left.parent = x
        # Changes y.parent since x, y swap happens
        y.parent = x.parent

        if x.parent == None:  # if x is root
            self.root = y  # y will be the top root

        elif x == x.parent.left:  # if x is a left child
            x.parent.left = y  # swap to y
        else:  # x is a right child
            x.parent.right = y  # swap to y

        # Now x is a y.left after rotation
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # L side
        y = x.left
        # Right rotate
        x.left = y.right
        # If y.right exists, set x as a parent
        if y.right != None:
            y.right.parent = x
        # Changes y.parent// since x, y swap happens
        y.parent = x.parent

        if x.parent == None:  # if x is root
            self.root = y  # y will be the top root

        elif x == x.parent.left:  # if x is a left child
            x.parent.left = y  # swap to y
        else:  # x is a right child
            x.parent.right = y  # swap to y

        # Now x is a y.right after rotation
        y.right = x
        x.parent = y

    def splay(self, n):
        while n.parent != None:  # node is not a root
            if n.parent == self.root:  # node is a child of root
                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)
            else:  # have to do several splays
                p = n.parent
                g = p.parent  # n's grandparent
                # LL -> RR rotation
                if n.parent.left == n and p.parent.left == p:
                    self.right_rotate(g)
                    self.right_rotate(p)
                # RR -> LL rotation
                elif n.parent.right == n and p.parent.right == p:
                    self.left_rotate(g)
                    self.left_rotate(p)
                #  RL -> LR rotation
                elif n.parent.left == n and p.parent.right == p:
                    self.right_rotate(p)
                    self.left_rotate(g)
                # LR -> RL rotation
                elif n.parent.right == n and p.parent.left == p:
                    self.left_rotate(p)
                    self.right_rotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        # run until finding n location
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y

        n.sum = n.data


        if y == None:  # newly added node is root
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n
        self.splay(n)
        print("=================n.data",  n.data)
        nl = self.inorder(n.left)

        nr = self.inorder(n.right)
        print("n.left: ", nl, "n.right: ", nr)
        n.sum = n.data + (nl if nl is not None else 0) + (nr if nr is not None else 0)
        print("n.sum: ", n.sum)




    def search(self, n, x):
        if n == None:
            return False
        if x == n.data:
            self.splay(n)
            return n
        elif x < n.data:
            return self.search(n.left, x)
        elif x > n.data:
            return self.search(n.right, x)
        else:
            return None

    def delete(self, n):
        # Splay the tree to n
        self.splay(n)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left  # set left subtree's root
        right_subtree = SplayTree()
        right_subtree.root = self.root.right  # set right subtree's root

        if left_subtree.root is not None:
            left_subtree.root.parent = None  # left top root is the top
        if right_subtree.root is not None:
            right_subtree.root.parent = None  # right top root is the top

        # Find the max in the left subtree
        if left_subtree.root is not None:
            m = left_subtree.maximum(left_subtree.root)
            # Set m as the top of the left subtree
            left_subtree.splay(m)
            # left subtree + right subtree
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root
        else:  # if no left subtree
            self.root = right_subtree.root

    def inorder(self, n):
        if n is not None:
            self.inorder(n.left)
            print(n.data)
            return n.data

            self.inorder(n.right)


if __name__ == "__main__":
    t = SplayTree()

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(5)

    t.insert(a)

    t.insert(b)

    t.insert(c)

    t.insert(d)
    t.inorder(t.root)

   # t.delete(a)
   # t.delete(d)
    #if t.search(t.root, 50):
      #  print("yes")
    #else:
     #   print("no")
    #print(t.search(t.root, 50))

