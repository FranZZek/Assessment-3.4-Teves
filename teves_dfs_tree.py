"""
Assessment 3.5 / 3.6: DFS Methods in Tree
Binary tree for the name: FRANZ TEVES (as drawn on paper)
Traversals: PreOrder, InOrder, PostOrder
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # ---------- DFS Traversals ----------
    def preorder(self, node, result):
        """Root -> Left -> Right"""
        if node:
            result.append(node.key)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result

    def inorder(self, node, result):
        """Left -> Root -> Right"""
        if node:
            self.inorder(node.left, result)
            result.append(node.key)
            self.inorder(node.right, result)
        return result

    def postorder(self, node, result):
        """Left -> Right -> Root"""
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.key)
        return result

    # ---------- Display ----------
    def display(self):
        """Draw the tree top-down, the way you would draw it on paper."""
        if self.root is None:
            return

        # Each node's column = its InOrder position, its row = its depth
        positions = {}
        counter = [0]

        def assign(node, depth):
            if node is None:
                return
            assign(node.left, depth + 1)
            positions[node] = (counter[0], depth)
            counter[0] += 1
            assign(node.right, depth + 1)

        assign(self.root, 0)

        spacing = 4
        max_depth = max(d for _, d in positions.values())
        grid = [[" "] * (counter[0] * spacing) for _ in range(max_depth * 2 + 1)]

        for node, (col, depth) in positions.items():
            x, y = col * spacing, depth * 2
            grid[y][x] = node.key

            link = y + 1  # row that holds the branch lines
            if node.left:
                lx = positions[node.left][0] * spacing
                grid[link][lx] = "┌"
                for i in range(lx + 1, x):
                    grid[link][i] = "─"
            if node.right:
                rx = positions[node.right][0] * spacing
                for i in range(x + 1, rx):
                    grid[link][i] = "─"
                grid[link][rx] = "┐"

            if node.left and node.right:
                grid[link][x] = "┴"
            elif node.left:
                grid[link][x] = "┘"
            elif node.right:
                grid[link][x] = "└"

        for row in grid:
            print("".join(row).rstrip())


def build_tree():
    """Builds the exact tree drawn on paper."""
    f = Node("F")
    r = Node("R")
    e1 = Node("E")   # first E (child of F)
    a = Node("A")
    t = Node("T")
    v = Node("V")
    e2 = Node("E")   # second E (child of the first E)
    n = Node("N")
    z = Node("Z")
    s = Node("S")

    f.left, f.right = r, e1
    r.left, r.right = a, t
    e1.left, e1.right = v, e2
    a.left, a.right = n, z
    e2.left = s

    return BinaryTree(f)


def main():
    tree = build_tree()

    print("Name: Franz Teves\n")
    print("Binary Tree Structure:")
    tree.display()

    print("\nDFS Traversals:")
    print("PreOrder  (Root, Left, Right):", " ".join(tree.preorder(tree.root, [])))
    print("InOrder   (Left, Root, Right):", " ".join(tree.inorder(tree.root, [])))
    print("PostOrder (Left, Right, Root):", " ".join(tree.postorder(tree.root, [])))


if __name__ == "__main__":
    main()
