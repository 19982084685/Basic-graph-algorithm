class Network(object):
    """
    流网络类
    """
    def __init__(self, node_num):
        self.__network = {}
        self.__node_set = {}
        self.__flow_network = []
        self.__flow_network = []  # 用于计算边上剩余容量的网络
        for i in range(node_num + 1):
            self.__flow_network.append([0] * (node_num + 1))
        self.__node_num = node_num
    def __has_edge(self, begin, end):
        """
        是否有某条边边
        :param begin:起点
        :param end: 终点
        :return: 有返回True,否则返回False
        """
        if self.__network.get(begin) is None:
            return False
        if self.__network.get(begin).get(end) is None:
            return False
        return True


    def add_edge(self, begin, end, capacity):
        """
        添加边
        :param begin: 起点
        :param end: 终点
        :param capacity:容量
        :return:
        """
        if self.__node_set.get(begin)is None:
            self.__node_set[begin] = 1
        if self.__node_set.get(end) is None:
            self.__node_set[end] = 1
        if self.__network.get(begin) is None:
            self.__network[begin] = {}
        self.__network.get(begin)[end] = capacity

    def get_capacity(self, begin, end):
        # 返回某条边的容量
        if not self.__has_edge(begin, end):
            return 0
        return self.__network.get(begin).get(end)

    def update_residual_capacity(self, begin, end, flow):
        """
        更新边的剩余容量
        :param begin:
        :param end:
        :param flow:
        :return:
        """
        self.__flow_network[begin][end] += flow
        self.__flow_network[end][begin] = -self.__flow_network[begin][end]
        return True
    def get_residual_capacity(self, begin, end):
        """
        获取边的剩余容量
        :param begin:
        :param end:
        :return:
        """
        if not self.__has_edge(begin, end):
            return 0-self.__flow_network[begin][end]
        return self.__network.get(begin).get(end) - self.__flow_network[begin][end]

    def change_flow_to(self, begin, end, new_flow):
        """
         改变边的容量
        :param begin:
        :param end:
        :param new_flow:
        :return:
        """
        if not self.__has_edge(begin, end):
            self.add_edge(begin, end, new_flow)
        self.__network.get(begin)[end] = new_flow

    def all_keys(self):
        """
        返回所有节点
        :return:
        """
        return self.__node_set.keys()

    def all_node(self):
        """
        返回所有有出边的节点
        :return:
        """
        return self.__network.keys()
    def all_neighbor(self, begin):
        """
        返回所有邻接节点
        :param begin:
        :return:
        """
        if self.__node_set.get(begin) is None:
            return None
        return self.__network[begin].keys()

    def get_node_num(self):
        """
        返回节点数目
        :return:
        """
        return self.__node_num