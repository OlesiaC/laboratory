class Node:
    def __init__(self, value, next_link=None):
        self.value = value
        self.next_link = next_link


node5 = Node(5)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

node3.next_link = node2


def is_looped(node):
    if node.next_link is node:
        return True
    current_node = node
    nodes = []
    while True:
        if current_node.next_link is None:
            return False
        next_node = current_node.next_link
        if next_node not in nodes:
            nodes.append(next_node)
            current_node = next_node.next_link
            continue
        else:
            return True


def test_linked_list_is_looped():
    print(is_looped(node1))


test_linked_list_is_looped()
