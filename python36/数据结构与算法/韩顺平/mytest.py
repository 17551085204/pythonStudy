# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/26 21:04         
'''
# import lib
 

# 完成走迷宫问题
import  numpy as np
class MiGong:
    '''
    规定 map[i][j]==0,代表这个点没有走过
    规定 map[i][j]==1,代表这个点是墙
    规定 map[i][j]==2,代表这个点可以走通
    规定 map[i][j]==0,代表这个点探测过，但是走不通

    '''
    map=np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1]
                  ])
    # 根据传入的i,j位置，设置地图上的点是否可以走通
    def setWay(self,map,i,j):
        if self.map[6][7]==2:
            return True
        else:
            if self.map[i][j]==0:
                self.map[i][j]=2
                if self.setWay(self.map,i+1,j): # 向下
                    return True
                elif self.setWay(self.map,i,j+1): # 向右
                    return True
                elif self.setWay(self.map,i-1,j): # 向上
                    return True
                elif self.setWay(self.map,i,j-1): # 向左
                    return True
                self.map[i][j]=3
                return  False
            else:
                return False

    def setMap(self):
        self.setWay(self.map,1,1)
        print(self.map)

# migong=MiGong()
# migong.setMap()


# 完成8皇后问题
class Queen:
    maxSize=0
    array=[]
    count=0
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.array=[0 for i in range(maxSize)]

    # 判断放置第n个皇后时，是否产生排斥
    def judge(self,n):
        for i in range(n):
            if self.array[i]==self.array[n] or (abs(n-i)==abs(self.array[n]-self.array[i])):
                return True
        return False

    # 放置第n个皇后
    def check(self,n):
        if n==self.maxSize: # 在放置第maxSize+1个皇后，说明前面的maxSize个皇后都已经放好位置了
            print(self.array)
            self.count=self.count+1
            return
        for i in range(self.maxSize):
            self.array[n]=i   # 尝试对这个位置依次填入 0~maxSize-1这些数字，并通过不断回溯判断是否产生排斥
            if not self.judge(n):
                self.check(n+1)  # 如果第n个皇后放置的位置确定后，不会产生排斥，就可以继续放第n+1个皇后了

    def printQueen(self):
        self.check(0)
        print('{0}皇后共有{1}种摆法'.format(self.maxSize,self.count))

queen=Queen(8)
queen.printQueen()
