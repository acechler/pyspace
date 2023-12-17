
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __repr__(self):
        return str(self.value)
    
    def add_edge(self, node):
        self.edges.append(node)
        node.edges.append(self)

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
    
    def add_node(self, node):
        self.nodes.append(node)

    def add_nodes(self, nodes):
        self.nodes.extend(nodes)
    
    def add_edge(self, node1, node2):
        node1.add_edge(node2)
    