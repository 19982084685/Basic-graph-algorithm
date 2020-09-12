from time import time
from heapq import heapify, heappop, heappush
import mygraph
def heap_dijkstra(graph, s):
    """
    堆实现迪杰斯特拉算法
    :param graph: 图
    :param s: 源节点
    :return: 各节点距离标记字典
    """
    n=graph.get_node_num()
    A=[99999]*n
    p=[0]*n
    node_s = (0, s)  # 源节点实体二元组（距离标记，节点）
    min_heap = list()     # 用于建堆的列表
    visited=[]
    A[s-1]=0
    min_heap.append(node_s)
    heapify(min_heap)         # 初始化最小堆
    while min_heap:
        min_node = heappop(min_heap)  # 取最小距离标记节点
        visited.append(min_node[1])
        node_neighbor_edges = graph.get_node_edges(min_node[1])  # 将所有邻接节点入堆
        for e in node_neighbor_edges:
            if (A[int(min_node[1])-1]+e[0]<A[int(e[2])-1]):
                A[int(e[2])-1]=A[int(min_node[1])-1]+e[0]
                p[int(e[2])-1]=int(min_node[1])
                heappush(min_heap, (A[int(e[2])-1], e[2]))
    print(A)
    return p
def printarr(s,p,d):
    d=int(d)
    s=int(s)
    while d!=s:
        print("% d <- % d"%(d,p[d-1]))
        d=p[d-1]
"""mg=mygraph.Graph()
data=mg
data.add_edge(mygraph.Edge(1,2,4))
data.add_edge(mygraph.Edge(1,3,3))
data.add_edge(mygraph.Edge(2,3,2))
data.add_edge(mygraph.Edge(2,4,1))
data.add_edge(mygraph.Edge(3,4,5))
par=bucket_dijkstra(data,1,5)
print(par)
printarr(1,par,4)"""
f=open('test-3.txt','r')
mydata=f.readlines()
g = mygraph.Graph()
for line in mydata[2:-2]:
    a,b,c=line.split()
    g.add_edge(mygraph.Edge(int(a),int(b),int(c)))
s=int(mydata[-2])
par=heap_dijkstra(g,s)
print(par)
d=int(mydata[-1])
printarr(s,par,d)
f.close()
