from time import time
from BucketSet import BucketSet
import mygraph
def bucket_dijkstra(graph, s, max_edge_weight):
    """
    桶实现的迪杰斯特拉算法
    :param graph: 图
    :param s: 源节点
    :param max_edge_weight: 最大边权
    :return: 距离字典
    """
    n=graph.get_node_num()
    A=[99999]*n
    p=[0]*n
    buckets = BucketSet(max_edge_weight+1)  # 创建循环桶对象
    node_s = (0, s)            # 源节点二元组（距离标记，节点）
    visited = []
    A[s-1]=0
    buckets.add_thing(node_s)       # 添加源节点到桶 
    while not buckets.is_empty():   # 所有的桶未空
        min_list = buckets.pop_min()  # 取最小距离标记集合 返回列表
        while not len(min_list) == 0:
            min_node = min_list.pop()
            visited.append(min_node[1])
            node_neighbor_edges = graph.get_node_edges(min_node[1])  # 将所有邻接节点加入桶中
            for e in node_neighbor_edges:
                if (A[int(min_node[1])-1]+e[0]<A[int(e[2])-1]):
                    A[int(e[2])-1]=A[int(min_node[1])-1]+e[0]
                    p[int(e[2])-1]=int(min_node[1])
                    buckets.add_thing((A[int(e[2])-1], e[2]))
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
f.close()
g = mygraph.Graph()    
max_edge_weight = 0
for line in mydata[2:-2]:
    a,b,c=line.split()    
    g.add_edge(mygraph.Edge(int(a),int(b),int(c)))
    if (max_edge_weight<int(c)):
        max_edge_weight=int(c)
s=int(mydata[-2])
par=bucket_dijkstra(g,s,max_edge_weight)
print(par)
d=int(mydata[-1])
printarr(s,par,d)