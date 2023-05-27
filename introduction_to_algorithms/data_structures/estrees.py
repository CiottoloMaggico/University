from data_structures import Tree, TreeNode, Queue, Node, Stack
import random

def build_tree(h):
    def recursive_build(node, h):
        if not h:
            return
        node.right = TreeNode(random.randint(0, 100))
        node.left = TreeNode(random.randint(0, 100))
        recursive_build(node.right, h-1)
        recursive_build(node.left, h-1)

    tree = Tree(TreeNode(random.randint(0, 100)))
    recursive_build(tree.root, h)
    return tree



def pos_to_fathers(a):
    p, c = [None] * len(a), [None] * len(a)
    p[0], c[0] = "/", a[0]
    for i in range(1,len(a),):
        father = (i-1)//2
        c[i] = a[i]
        p[i] = father
    return p,c

def fathers_to_pos(f, k, a, i):
    if i >= len(a):
        return a
    if i == -1:
        for j in range(len(f)):
            if f[j] == "/":
                a[i+1] = k[j]
                return fathers_to_pos(f, k, a, i+1)
    child = 2*i+1
    for j in range(len(f)):
        if f[j] != "/" and k[f[j]] == a[i]:
            a[child] = k[j]
            if child == 2*i+2:
                fathers_to_pos(f, k, a, child)
                fathers_to_pos(f, k, a, child-1)
            child += 1

def node_counter(tree):
    def recursive_traversal(node):
        if node == None:
            return 0
        return 1 + recursive_traversal(node.right) + recursive_traversal(node.left)

    return recursive_traversal(tree.root)

def find(tree, t):
    def recursive_traversal(node, t):
        if node == None:
            return False
        if node.key == t:
            return True
        return recursive_traversal(node.right, t) or recursive_traversal(node.left, t)

    return recursive_traversal(tree.root, t)

def level_traverse(tree):
    def recursive_traversal(node, queue):
        if node == None:
            return
        if node.right:
            queue.push(node.right)
        if node.left:
            queue.push(node.left)
        deleted = queue.pop()
        print(deleted)
        recursive_traversal(queue.head, queue)

    recursive_traversal(tree.root, Queue(tree.root))

def iterative_preorder(tree):
    my_stack = Stack(TreeNode(tree.root.key))
    while my_stack.head != None:
        node = my_stack.pop()
        print(node.key)
        if node.left != None:
            my_stack.push(node.left)
        if node.right != None:
            my_stack.push(node.right)


def pos_preorder(a, i, h=0):
    if i >= len(a):
        return ""
    repr = f"{' '*h}{a[i]}\n"
    repr += pos_preorder(a, 2*i+1, h+1)
    repr += pos_preorder(a, 2*i+2, h+1)
    return repr

def valid_nodes(node, sum=0):
    if node == None:
        return 0
    if node.key == sum:
        print(f"is valid node: {node.key}")
        sum += node.key
        return 1 + valid_nodes(node.right, sum) + valid_nodes(node.left, sum)
    sum += node.key
    return valid_nodes(node.right, sum) + valid_nodes(node.left, sum)


if __name__ == "__main__":
    # Test representation converter
    pos_representation = [0, 2, 5, 1, 7, 6, -40, None, None, 9]
    father_representation = pos_to_fathers(pos_representation)
    a = [None]*len(father_representation[0])
    print(f"Original: {pos_representation}")
    print(f"Father: {father_representation}")
    fathers_to_pos(*father_representation, a, -1)
    print(f"Rebuild: {a}")

    # Test build tree
    my_tree = build_tree(3)
    print(my_tree)
    #Test node counter
    print(f"Number of nodes: {node_counter(my_tree)}\n")
    # Test find node
    t = int(input("What number you want search: "))
    print(f"Is in the tree? {find(my_tree, t)}")
    # Test level traversal
    print("Level traversal")
    level_traverse(my_tree)
    # Test iterative preorder traversal
    print("Iterative traversal")
    iterative_preorder(my_tree)
    # Test pos preorder traversal
    print("Pos Traversal")
    print(pos_preorder(pos_representation, 0))
    # Test valid nodes
    print(f"Valid nodes: {valid_nodes(my_tree.root)}")