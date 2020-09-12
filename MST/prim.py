from collections import defaultdict

class Heap():

    def __init__(self):
        self.array = []#用数组形式存储堆的树结构
        self.size = 0#堆内节点个数
        self.pos = []#判断节点是否在堆中

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # 交换堆中两个节点
    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, idx):#递归，下滤根节点
        #符合完全二叉树中，索引规律
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        print(self.array,self.size)
        print(self.pos)

        if left < self.size and self.array[left][1] < \
                                self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < \
                                self.array[smallest][1]:
            smallest = right
        #最终smallest为三个点中最小的那个的索引，非左即右

        # smallest将与左或右节点交换
        if smallest != idx:

            # Swap positions
            self.pos[ self.array[smallest][0] ] = idx
            self.pos[ self.array[idx][0] ] = smallest

            # Swap nodes
            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    # 抽取堆中最小节点
    def extractMin(self):

        if self.isEmpty() == True:
            return

        # 找到根节点
        root = self.array[0]

        # 把最后一个节点放在根节点上去
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
        print()
        print('当前堆最后面位置的元素为',lastNode)

        # 更新根节点和最后一个节点的pos
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1#此时堆大小已经减小1

        # 减小size，从根节点开始从新构造
        self.size -= 1
        self.minHeapify(0)

        return root#返回的是被替换掉的那个

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):#上滤节点

        # 获得v在堆中的位置
        i = self.pos[v]

        # 更新堆中v的距离为dist，虽说是更新，但肯定是减小key
        self.array[i][1] = dist

        # 一直寻找i的父节点，检查父节点是否更大
        while i > 0 and self.array[i][1] < self.array[int((i - 1) / 2)][1]:

            # pos数组交换，array也得交换
            self.pos[ self.array[i][0] ] = int((i-1)/2)
            self.pos[ self.array[int((i-1)/2)][0] ] = i
            self.swapMinHeapNode(i, int((i - 1)/2) )

            # i赋值为父节点索引
            i = int((i - 1) / 2)

    # 检查v是否在堆中，很巧妙的是，由于size一直在减小
    # 当pos小于size说明该点在堆中不可能的位置，即不在堆中
    def isInMinHeap(self, v):

        if self.pos[v] < self.size:
            return True
        return False


def printArr(parent, n):
    for i in range(1, n):
        print ("% d - % d" % (parent[i]+1, i+1))


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # 添加无向图的每条边
    def addEdge(self, src, dest, weight):

        # 当前边从src到dest，权值为weight
        # 添加到src的邻接表中，添加元素为[dest, weight]
        # 注意都是添加到0索引位置
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        # 因为是无向图，所以反向边也得添加
        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    # 主函数用来构造最小生死树（MST）
    def PrimMST(self):
        # V是节点的个数
        V = self.V  

        # 存每个节点的key值
        key = []   

        # 记录构造的MST
        parent = [] 

        # 建立最小堆
        minHeap = Heap()

        # 初始化以上三个数据结构
        for v in range(V):
            parent.append(-1)#初始时，每个节点的父节点是-1
            key.append(float('inf'))#初始时，每个节点的key值都是无穷大
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) )
            #newMinHeapNode方法返回一个list，包括节点id、节点key值
            #minHeap.array成员存储每个list，所以是二维list
            #所以初始时堆里的每个节点的key值都是无穷大
            minHeap.pos.append(v)
            #pos成员添加每个节点id
        #minHeap.pos初始时是0-8，都小于9即节点数

        minHeap.pos[0] = 0#不懂这句，本来pos的0索引元素就是0啊
        key[0] = 0#让0节点作为第一个被挑选的节点
        minHeap.decreaseKey(0, key[0])
        #把堆中0位置的key值变成key[0]，函数内部重构堆

        # 初始化堆的大小为V即节点个数
        minHeap.size = V
        sum=0
        print('初始时array为',minHeap.array)
        print('初始时pos为',minHeap.pos)
        print('初始时size为',minHeap.size)

        # 最小堆包含所有非MST集合中的节点
        # 所以当最小堆为空，循环终止
        while minHeap.isEmpty() == False:

            # 抽取最小堆中key值最小的节点
            newHeapNode = minHeap.extractMin()
            print('抽取了最小元素为',newHeapNode)
            sum=sum+newHeapNode[1]
            u = newHeapNode[0]

            # 遍历所有的邻接点然后更新它们的key值
            for pCrawl in self.graph[u]:

                v = pCrawl[0]

                # 如果v在当前最小堆中，且新的key值比当前key值更小，就更新
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u

                    # 也更新最小堆中节点的key值，重构
                    minHeap.decreaseKey(v, key[v])

        printArr(parent, V)
        print("The weigeh sum is ",sum)

f=open('test-1.txt','r')
mydata=f.readlines()
n=mydata[1]
g = Graph(int(n))
for line in mydata[2:]:
    a,b,c=line.split()
    g.addEdge(int(a)-1, int(b)-1, int(c))
f.close()
g.PrimMST()