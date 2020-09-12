from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V= vertices #顶点的数量
        self.graph = [] # 二维list用来存边的起点、终点、权重

    # 添加每条边
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    # 递归找到每个节点所在子树的根节点
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # 联合两颗子树为一颗子树，谁附在谁身上的依据是rank
    def union(self, parent, rank, x, y, xroot, yroot):
        #xroot = self.find(parent, x)不需要重复此函数
        #yroot = self.find(parent, y)不需要重复此函数

        #进行路径压缩
        if(xroot != parent[x]):
            parent[x] = xroot
        if(yroot != parent[y]):
            parent[y] = yroot 

        # Attach smaller rank tree under root of high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1
    def KruskalMST(self):

        result =[] #存MST的每条边

        i = 0 # 用来遍历原图中的每条边，但一般情况都遍历不完
        e = 0 # 用来判断当前最小生成树的边数是否已经等于V-1

        #按照权重对每条边进行排序，如果不能改变给的图，那么就创建一个副本，内建函数sorted返回的是一个副本
        self.graph =  sorted(self.graph,key=lambda item: item[2])

        parent = [] ; rank = []

        # 创建V个子树，都只包含一个节点
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # MST的最终边数将为V-1
        while e < self.V -1 :

            # 选择权值最小的边，这里已经排好序
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            # 如果没形成边，则记录下来这条边
            if x != y:
                #不等于才代表没有环
                e = e + 1    
                result.append([u,v,w])
                self.union(parent, rank, u, v, x, y)            
            # 否则就抛弃这条边
        sum=0
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            print ("%d -- %d == %d" % (u+1,v+1,weight))
            sum=sum+weight
        print("The weight sum is ",sum)

f=open('test-3.txt','r')
mydata=f.readlines()
f.close()
n=mydata[1]
g = Graph(int(n))
for line in mydata[2:]:
    a,b,c=line.split()
    g.addEdge(int(a)-1, int(b)-1, int(c))
g.KruskalMST()