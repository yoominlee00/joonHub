import sys
class Node:
    def __init__(self, value = None, lvalue = None,rvalue = None):
        self.value =value
        self.left = lvalue
        self.right =rvalue
nodes = {}
result1 = []
result2 = []
result3 = []
N = int(input())
for _ in range(N):
    parent, left, right = list(map(str,sys.stdin.readline().split()))

    # 지금 노드 목록에 없으면?
    if parent not in nodes:
        nodes[parent] = Node(parent)
    current = nodes[parent]

    if left != '.':
        if left not in nodes:
            nodes[left] = Node(left)
        current.left = nodes[left]

    if right != '.':
        if right not in nodes:
            nodes[right] = Node(right)
        current.right = nodes[right]
tree = nodes[parent]

def circ1(node):
    if not node:
        return
    result1.append(node.value)
    circ1(node.left)
    circ1(node.right)

def circ2(node):
    if not node:
        return
    circ2(node.left)
    result2.append(node.value)
    circ2(node.right)

def circ3(node):
    if not node:
        return
    circ3(node.left)
    circ3(node.right)
    result3.append(node.value)

circ1(nodes['A'])
circ2(nodes['A'])
circ3(nodes['A'])
print(''.join(map(str,result1)))
print(''.join(map(str,result2)))
print(''.join(map(str,result3)))