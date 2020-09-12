
"""
边类，包含边链接的两个节点和边的权值
"""
class Edge(object):
    def __init__(self, node_a, node_b, weight):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = int(weight)

    def get_node_a(self):
        return self.node_a

    def get_node_b(self):
        return self.node_b

    def get_weight(self):
        return self.weight
