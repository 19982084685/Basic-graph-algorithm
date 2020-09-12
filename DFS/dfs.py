
class Graph(object):
    'Undirect Unweighted Graph coutainer'
    def __init__(self):#初始化
        self.nodes=list()
        self.edge=dict()
        self.startnode=0
        self.endnode=0
        self.nodesum=0
        self.edgesum=0
    def insert(self,a,b):#插入操作
        'insert edges into graph'
        if not(a in self.nodes):
            self.nodes.append(a)
            self.edge[a]=list()
        if not(b in self.nodes):
            self.nodes.append(b)
            self.edge[b]=list()
        if not(a in self.edge[b]):#因为是无向图，所以条件可以这样写
            self.edge[a].append(b)
            self.edge[b].append(a)
    #def succ(self,a):
        #return self.edge[a]
    def getnodes(self):
        return self.nodes
    def countnodes(self):
        return len(self.nodes)
    def countedges(self):
        return len(self.edge)



graph=Graph()
f=open('test-6.txt','r')##打开输入文件
mydata=f.readlines()
graph.nodesum=mydata[0]#节点数
graph.edgesum=mydata[1]#边数
graph.startnode=mydata[-2]#起点
graph.endnode=mydata[-1]#终点
for line in mydata[2:-2]:
    a,b=line.split()
    graph.insert(a,b)#构造邻接链表
f.close()
#print(graph.getnodes())
#print(graph.edge)
#print(graph.startnode)
#print(graph.endnode)
#print([graph.succ(x) for x in graph.nodes])


mygraph=graph
def front(a):
    return a[-1]##查看栈顶元素
def dfs(u):##用递归的方式找到全部路径
    
    u=int(u)
    mark[u-1]=1##将u标记为已探索
    B.append(u)##u入栈
    d=front(B)
    if (u==int(mygraph.endnode)):##如果u就是目标节点，直接输出B即为路径
        #print(B)
        global k
        k=k+1
        B.pop()
        mark[u-1]=0##将u弹出且标记置零，防止其对下一条路径搜索产生影响
        return
    for i in mygraph.edge[str(u)]:##如果u不为目标节点，则遍历它的相邻节点
        i=int(i)
        if mark[i-1]==0:
            dfs(i)##如果节点未被探索过，则对其使用递归
            mark[i-1]=0
    B.pop()##每结束一次dfs将末尾节点出栈，实现回溯到上一节点
B=[]
mark=[];
for i in range(0,int(mygraph.countnodes())):
    mark.append(0)##创建mark对节点状态进行标识，且用循环将其置为初始值0
k=0
dfs(mygraph.startnode)
print(k)