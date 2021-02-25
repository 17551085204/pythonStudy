# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/25 17:09         
'''
# import lib

# 八皇后问题

class Queen:
    maxSize=0
    array=[]
    count=0
    judgeCount=0
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.array = [0 for i in range(maxSize)]
    # 判断，当放置第n个皇后时，该皇后是否和前面已经摆放的皇后发生冲突
    def judge(self,n): # n=0,1,2,..7
        self.judgeCount=self.judgeCount+1
        for i in range(n):
            # 在同一列或者在斜线上
            if self.array[i]==self.array[n] or abs(self.array[i]-self.array[n])==abs(i-n):
                return False
        return True

    # 放置第n个皇后
    def check(self,n):
        if n==self.maxSize: # 再放第9个皇后，说明8个皇后已经放好了
            with open('queen.txt','a') as f:
                f.write(str(self.array))
                f.write('\n')

            print(self.array)
            self.count=self.count+1
            return
        for i in range(self.maxSize):
            self.array[n]=i
            if self.judge(n): # 不冲突
                self.check(n+1)
    # 递归打印8皇后所有的摆放方式
    def printQueen(self):
        self.check(0)
        print('{0}皇后共有{1}种摆放方式'.format(self.maxSize,self.count))
        print('判断中间过程的摆放是否冲突的次数为:{}'.format(self.judgeCount))

queen=Queen(8)
queen.printQueen()




