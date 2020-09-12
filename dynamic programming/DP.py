class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[1]*len(nums)
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    a[i]=max(a[i],a[j]+1)
        return max(a)
g=Solution()
f=open('sample.txt','r')
mydata=f.readlines()
f.close()
n=mydata[0]
for line in mydata[1:]:
    line=line.strip()
    line=list(line.split(' '))
    line=list(map(int,line))
    print(g.lengthOfLIS(line))