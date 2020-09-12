import queue
from copy import deepcopy
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




class Graph(object):
    def __init__(self):
        self.nodes = list()
        self.edge_num = 0
        self.edges = {}

    def get_node_edges(self, node):
        """
        返回该节点的所有邻接边
        :param node:
        :return: 邻接边
        """
        return deepcopy(self.edges[str(node)])

    # 获取链接字典并转换为string
    def to_string(self):
        """
        将图转换为string
        :return: str
        """
        return str(deepcopy(self.edges))

    def get_all_edges(self):
        """
        返回所有边
        :return: 所有边
        """
        es = list()
        for v in self.edges.values():
            es.append(v)
        return deepcopy(es)

    def get_node_num(self):
        """
        返回节点个数
        :return:
        """
        return len(self.nodes)

    # 返回边数
    def get_edge_num(self):

        return self.edge_num

    # 返回节点列表
    def get_node_list(self):
        return deepcopy(self.nodes)

    # 获取总权重
    def get_weight(self):
        weight = 0
        for edge in self.get_all_edges():
            weight += edge[0]
        return weight


    # 增加边，边在图中以三元组edge(node_a,node_b,weight)实现
    def add_edge(self, edge):
        node_a = edge.get_node_a()
        node_b = edge.get_node_b()
        weight = edge.get_weight()
        if not str(node_a) in self.nodes:
            self.nodes.append(str(node_a))
            self.edges[str(node_a)] = list()
        if not (str(node_b) in self.nodes):
            self.nodes.append(str(node_b))
            self.edges[str(node_b)] = list()
        if not ((weight, str(node_a), str(node_b)) in self.edges[str(node_a)]):
            self.edges[str(node_a)].append((weight, str(node_a), str(node_b)))
            self.add_edge_num()


    def add_edge_num(self):
            self.edge_num += 1