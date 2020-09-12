from time import time
from queue import Queue
from heapq import heapify, heappop, heappush
from Network import Network
from queue import PriorityQueue
class PushRelabel(object):
    __INF = 0xffffffff

    def __init__(self, start, des, network):
        self.__network = network   # 原网络
        self.__new_network = Network(network.get_node_num())  # bfs重构网络
        self.__high = [0] * (network.get_node_num() + 1)      # 高度函数
        self.__start = start          # 源点
        self.__des = des              # 汇点
        self.__Re_flow = [0] * (network.get_node_num() + 1)  # 盈余标记
        self.__node_heap = []             # 最小堆，用于获取最大高度盈余节点


    def __pre_flow(self):                # 推送预流
        self.__high[self.__start] = self.__new_network.get_node_num()  # 初始化高度源点高度
        for i in self.__new_network.all_neighbor(self.__start):
            if self.__new_network.get_capacity(self.__start, i) > 0:
                flow = self.__new_network.get_capacity(self.__start, i)    # 饱和推送
                self.__new_network.update_residual_capacity(self.__start, i, flow)  # 更新边的剩余容量
                self.__Re_flow[self.__start] -= flow   # 更新盈余量
                self.__Re_flow[i] += flow
                if i != self.__des:     # 将盈余节点放入堆中，高度取相反数
                    heappush(self.__node_heap, (-self.__high[i], i))

    def __push(self, begin, end):   # 推送
        """
        推送方法
        :param begin: 出发点
        :param end: 终点
        :return: null
        """
        flow = min(self.__Re_flow[begin], self.__new_network.get_residual_capacity(begin, end))   # 计算可推送的流大小
        self.__new_network.update_residual_capacity(begin, end, flow)  # 更新边上剩余容量
        self.__Re_flow[begin] -= flow      # 更新节点盈余流量
        self.__Re_flow[end] += flow
        if self.__Re_flow[begin] > 0:
            # heappush(self.__node_heap, (-self.__high[begin], begin))
            self.__push_relabel(begin)
        if (end != self.__des) and (end != self.__start):    # 推送目的点入堆
            heappush(self.__node_heap, (-self.__high[end], end))

    def __push_relabel(self, node):  # 推送重标记
        min_high = self.__INF        # 邻接节点最小高度
        min_node = 0                 # 最小高度邻接节点
        if self.__Re_flow[node] > 0:  # 有盈余
            for i in self.__new_network.all_keys():
                if self.__new_network.get_residual_capacity(node, i) > 0:  # 边上剩余容量>0
                    if min_high > self.__high[i]:
                        min_high = self.__high[i]
                        min_node = i
            if min_high == self.__INF:  # 高度达到上界就返回
                return
            # print(str(self.__high[node])+','+str(min_high))
            # self.test()
            if self.__high[node] == min_high + 1:   # 推送
                self.__push(node, min_node)
            if self.__high[node] < min_high + 1:
                self.__high[node] = min_high + 1    # 重标记
                self.__push(node, min_node)         # 推送


    def __bfs(self):       # 反向bfs, 网络重构
        """
        反向bfs重构网络并初始化高度；
        对于bfs算法结束后高度仍是0的节点，它们是无法到达汇点的，
        向这些节点推送流是毫无意义的，故重构网络，将这些节点剔除
        :return: 如果不能到达源点返回False,否者返回True
        """
        queue = PriorityQueue()        # 最小优先队列，保证跳数是最小跳数
        high = self.__high
        in_queue = {}                  # 在队列中标记
        queue.put((high[self.__des], self.__des))    # 汇点入队
        in_queue[self.__des] = 1                    # 标记为在队列中
        while not queue.empty():                # 队列非空
            m = queue.get()                     # 出队
            node = m[1]
            h = m[0]
            if h > self.__high[node]:       # 如果高度大于当前高度，不会更新高度，执行continue
                continue
            in_queue[node] = None           # 标记为不在队列中
            for i in self.__network.all_keys():
                if (self.__network.get_capacity(i, node) > 0) and (i != self.__des):  # 存在入边，且不是汇点
                    flow = self.__network.get_capacity(i, node)
                    self.__new_network.add_edge(i, node, flow)       # 网络重构
                    # print(str(node)+"\t"+str(i)+"\t"+str(flow))
                    if self.__high[i] == 0 and node != self.__start:                          # 如果当前高度为0，就更新高度
                        self.__high[i] = self.__high[node] + 1
                        queue.put((high[i], i))                      # 入队

        if self.__high[self.__start] == 0:            # 如果循环结束，源点的高度为0，说明到达不了源点，返回
            return False
        return True

    def get_max_flow(self):
        """
        获取最大流
        :return: 算法结束时返回汇点盈余，即是最大流
        """
        if not self.__bfs():  # bfs重构网络以及初始化高度
            return 0          # 如果bfs返回False，最大流为0
        heapify(self.__node_heap)     # 建堆
        self.__pre_flow()             # 预流推送

        while self.__node_heap:
            m = heappop(self.__node_heap)   # 取最大高度盈余节点
            node = m[1]
            self.__push_relabel(node)          # 推送重标记

        return self.__Re_flow[self.__des]   # 返回最大流

    def test(self):
        """
        测试函数，看是否满足循环不变式
        :return:
        """
        print("test")
        for i in self.__new_network.all_node():
            h = 0xffffffff
            min_node = 0

            for j in self.__new_network.all_neighbor(i):
                if h > self.__high[j]:
                   h = self.__high[j]
                   min_node = j
            if self.__high[i] > (h+1) and i != self.__start and self.__Re_flow[i]>0:

                print("test:"+str(i)+','+str(min_node))
                print(self.__Re_flow[i])
    def test2(self, i):
        h = 9999
        for j in self.__new_network.all_neighbor(i):
            h = min(h, self.__high[j])
        if self.__high[i] > (h + 1) and i != self.__start:
            print("test:" + str(i))
            print(self.__Re_flow[i])


