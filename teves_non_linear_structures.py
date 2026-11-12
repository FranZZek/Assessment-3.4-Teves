"""
Assessment 3.3: Non-Linear Data Structure
Last Name: TEVES

Part 1: Binary Tree (BFS and DFS)
Part 2: Graph, undirected (BFS and DFS)
"""

from collections import deque


# ---------------------------------------------------------------------------
# PART 1: BINARY TREE
# ---------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    """Algorithm A: build the binary tree."""
    root = Node("V")
    root.left = Node("E")        # E-left
    root.right = Node("E")       # E-right
    root.left.left = Node("T")
    root.left.right = Node("S")
    return root


def tree_bfs(root):
    """Algorithm B: BFS / level-order traversal using a queue."""
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def preorder(node, result):
    """Algorithm C: Root, Left, Right."""
    if node is None:
        return
    result.append(node.data)
    preorder(node.left, result)
    preorder(node.right, result)


def inorder(node, result):
    """Algorithm C: Left, Root, Right."""
    if node is None:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)


def postorder(node, result):
    """Algorithm C: Left, Right, Root."""
    if node is None:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.data)


# ---------------------------------------------------------------------------
# PART 2: GRAPH
# ---------------------------------------------------------------------------
class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        self.adj.setdefault(v, [])

    def add_edge(self, u, v):
        """Undirected edge."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        """Algorithm E: BFS using a queue and a visited set."""
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in self.adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        """Algorithm F: recursive DFS using a visited set."""
        visited = set()
        result = []

        def visit(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return result


def build_graph():
    """Algorithm D: build the graph (E1 = level-1 E, E2 = level-2 E)."""
    g = Graph()
    for v in ["T", "S", "E1", "V", "E2"]:
        g.add_vertex(v)
    g.add_edge("T", "S")
    g.add_edge("T", "E1")
    g.add_edge("T", "V")
    g.add_edge("S", "E2")
    return g


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=== BINARY TREE (TEVES) ===")
    root = build_tree()
    print("BFS (level-order):", " -> ".join(tree_bfs(root)))

    pre, ino, post = [], [], []
    preorder(root, pre)
    inorder(root, ino)
    postorder(root, post)
    print("DFS Preorder     :", " -> ".join(pre))
    print("DFS Inorder      :", " -> ".join(ino))
    print("DFS Postorder    :", " -> ".join(post))

    print("\n=== GRAPH (TEVES) ===")
    g = build_graph()
    print("Adjacency list:")
    for vertex, neighbors in g.adj.items():
        print(f"  {vertex}: {', '.join(neighbors)}")
    print("BFS from T:", " -> ".join(g.bfs("T")))
    print("DFS from T:", " -> ".join(g.dfs("T")))


if __name__ == "__main__":
    main()
