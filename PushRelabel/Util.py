import random

from Edge import Edge
def create_topology(node_num, edge_num, max_weight, file_path):
    """
    生成有向随机拓扑
    :param node_num: 节点数
    :param edge_num: 边数
    :param max_weight: 最大权重，表示权重范围在（0，max_weight）之间
    :param file_path: 数据写入文件路径
    :return:
    """
    NODE_NUM = node_num               # 节点数
    EDGE_NUM = edge_num               # 边数
    MAX_WEIGHT = max_weight           # 最大权重
    list_nodes = {}                   # 节点邻接字典
    neighbor_nodes = {}
    tree_nodes = []
    list_nodes[str(1)] = list()
    neighbor_nodes[str(1)] = list()
    tree_nodes.append(1)
    for i in range(2, NODE_NUM+1):
        tree_nodes.append(i)
        list_nodes[str(i)] = list()
        neighbor_nodes[str(i)] = list()
        new_edge = Edge(random.randint(1, i - 1), i, random.randint(1, MAX_WEIGHT))# 随机生成一条边
        neighbor_nodes[str(new_edge.get_node_a())].append(str(new_edge.get_node_b()))
        list_nodes[str(new_edge.get_node_a())].append(new_edge)
    with open(file_path, 'a') as file:
         for key in list_nodes.keys():
             node_a = key
             for edge in list_nodes[key]:
                node_b = edge.get_node_b()
                weight = edge.get_weight()
                file.write(str(node_a)+'\t'+str(node_b)+'\t'+str(weight)+'\n')
         file.close()

    """
    第二步：随机在两个节点之间添加边
    """
    for i in range(1, EDGE_NUM-NODE_NUM+2):
        while True:
            node_1 = random.randint(1, NODE_NUM)     # 随机选两个节点连线
            node_2 = random.randint(1, NODE_NUM)
            if node_1 != node_2:                     # 边连接的两个节点不是同一个点
                if str(node_2) not in neighbor_nodes[str(node_1)]:     # 如果这两个节点未曾连线
                    # 将该条边加入到
                    new_edge = Edge(node_1, node_2, random.randint(1, MAX_WEIGHT))
                    list_nodes[str(new_edge.get_node_a())].append(new_edge)
                    neighbor_nodes[str(node_1)].append(str(node_2))
                    # 将该条边
                    with open(file_path, 'a') as file:
                        file.write(str(node_1) + '\t' + str(node_2)+'\t'+str(new_edge.get_weight()) + '\n')
                        file.close()
                    break


# 清空文件
def clear_file(file_path):
    """
    清空指定路径文件
    :param file_path: 文件路径
    :return:
    """
    with open(file_path, 'w') as f:
        f.truncate()
        f.close()

# 创建一个网络
# def create_network(network, file_path):
#     """
#     读取文件创建流网络
#     :param network:
#     :param file_path:
#     :return:
#     """
#     with open(file_path, 'r') as file:
#         for line in file.readlines():
#             begin, end, capacity = line.split()
#             channel = Channel(int(begin), int(end), capacity, True)
#             network.add_channel(channel)
#         file.close()

def create_network(network, file_path):
    """
    读取文件创建流网络
    :param network:
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as file:
        for line in file.readlines():
            begin, end, capacity = line.split()
            network.add_edge(int(begin), int(end), int(capacity))
        file.close()

def write(file_path, text):
    with open(file_path, 'a') as file:
        file.write(str(text)+'\t')
        file.close()