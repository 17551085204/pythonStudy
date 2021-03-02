# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/27 16:19         
'''
# import lib
 

'''
1,走迷宫问题
2,8皇后问题
'''
import numpy as np

class MiGong:
    '''
    map[i][j]==0  没有走过
    map[i][j]==1  墙
    map[i][j]==2  可以走通
    map[i][j]==3  走过，但是没有走通
    '''
    map=np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1]
                  ])
    # 从第[i][j]这个位置开始走迷宫
    def setWay(self,map,i,j):
        if map[len(map)-2][len(map[0])-2]==2: # 代表最后一个位置可以走通，那么前面就有了一条通路
            return True
        if map[i][j]==0:
            map[i][j]=2
            if self.setWay(map,i+1,j): # 向下
                return True
            elif self.setWay(map,i,j+1): # 向右
                return True
            elif self.setWay(map,i-1,j): # 向上
                return True
            elif self.setWay(map,i,j-1): # 向左
                return True
            map[i][j]=3
            return False

    def getWay(self):
        self.setWay(self.map,1,1)
        print(self.map)

# migong=MiGong()
# migong.getWay()

class Queen:
    array=[]
    maxSize=0
    count=0
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.array=[0 for i in range(maxSize)] # 需要将其初始化为 长度为maxSize的数组

    # 判断放入第n个皇后是否会发生排斥
    def judge(self,n):
        for i in range(n):
            if self.array[i]==self.array[n] or abs(n-i)==abs(self.array[n]-self.array[i]):
                return True  # 代表会发生排斥
        return False # 代表不会发生排斥

    # 放入第n个皇后
    def check(self,n):
        if n==self.maxSize: # 在放第maxSize+1个皇后了，说明前面maxSize个皇后都已经放好了
            print(self.array)
            self.count=self.count+1
            return
        for i in range(self.maxSize):
            self.array[n]=i # 在第n个位置依次赋值 0,1,..maxSize-1进行尝试，看看是否可以加入
            if not self.judge(n):
                self.check(n+1) # 如果不发生排斥，就可以继续放第n+1个皇后

    # 打印所有摆放方式，用数组形式。
    def printQueen(self):
        self.check(0)
        print('{0}皇后共有{1}种不同的解法'.format(self.maxSize,self.count))

queen=Queen(8)
queen.printQueen()




