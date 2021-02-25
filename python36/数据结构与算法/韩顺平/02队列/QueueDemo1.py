# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/20 16:20         
'''
# import lib
 

# 数组模拟队列
# 最简单的实现，没有实现循环队列功能
class arrayQueue:
    real=0
    front=-1 # 指向队列头的前一个元素
    maxSize=-1 # 指向队列尾元素
    array=[]
    def __init__(self,maxSize): #self必须位于第一个参数
        self.real = -1
        self.front=-1
        self.maxSize=maxSize # 数组的最大容量
        for i in range(maxSize):
            self.array.append(0)

    # 查看此时队列头数据
    def headQueue(self):
        if self.real==self.front:
            print('队列为空，没有头数据')
            return None
        else:
            return self.array[self.front+1]

    # 队列中添加数据
    def addQueue(self,number):
        if self.real<self.maxSize-1:
            self.real=self.real+1
            self.array[self.real]=number
        else:
            print('队列已经满了~')

    # 队列中取出数据
    def getQueue(self):
        if self.real==self.front:
            print('队列为空，无法取数据')
            return None
        else:
            res= self.array[self.front+1]
            self.front=self.front+1
            return res

    # 打印目前队列中的数据
    def showQueue(self):
        if self.front==self.real:
            print('队列为空')
        else:
            print('此时队列中的数据为:',end='')
            for i in range(self.front+1,self.real+1):
                print(self.array[i],end=' ')
            print()

# 创建队列
queue=arrayQueue(4)
# 添加元素
queue.addQueue(1)
queue.addQueue(2)
queue.addQueue(3)
queue.addQueue(4)
# queue.addQueue(5)

# 取出元素
res1=queue.getQueue()
print('取出的数据为',res1)
# res2=queue.getQueue()
# print('取出的数据为',res2)
# res3=queue.getQueue()
# print('取出的数据为',res3)
# res4=queue.getQueue()
# print('取出的数据为',res4)

# res5=queue.getQueue()
# print('取出的数据为',res5)

# 查看队列头数据
head=queue.headQueue()
print('此时队列头数据为：',head)

# 打印队列所有元素
queue.showQueue()


