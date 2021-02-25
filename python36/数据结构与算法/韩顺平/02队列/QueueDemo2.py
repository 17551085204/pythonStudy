# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/20 16:20         
'''
# import lib

# 数组模拟队列
# 实现循环队列功能，实现数组复用
class arrayQueue:
    real=0 # 指向队列尾的后一个元素，预留出一个位置
    front=0 # 指向队列头元素
    maxSize=0
    array=[]
    def __init__(self,maxSize): #self必须位于第一个参数
        self.real = 0
        self.front= 0
        self.maxSize=maxSize+1 # 数组的最大容量
        for i in range(self.maxSize):
            self.array.append(0)

    # 查看此时队列头数据
    def headQueue(self):
        if self.real==self.front:
            print('队列为空，没有头数据')
            return None
        else:
            return self.array[self.front]

    # 队列中添加数据
    def addQueue(self,number):
        if (self.real+1)%self.maxSize==self.front:
            print('队列已经满了~')
        else:
            self.array[self.real] = number
            self.real = (self.real + 1)%self.maxSize

    # 队列中取出数据
    def getQueue(self):
        if self.real==self.front:
            print('队列为空，无法取数据')
            return None
        else:
            res= self.array[self.front]
            self.front=(self.front+1)%self.maxSize
            return res

    # 打印目前队列中的数据
    def showQueue(self):
        if self.front==self.real:
            print('队列为空')
        else:
            print('此时队列中的数据为:',end='')
            # 从队列元素开始位置打印，front开始，总共元素有 (self.real+self.maxSize-self.front)%self.maxSize
            for i in range(self.front,self.front+(self.real+self.maxSize-self.front)%self.maxSize):
                print(self.array[i%self.maxSize],end=' ') # i会超出maxSize，所以需要取模
            print()


if __name__ == '__main__':
    # 创建队列
    queue = arrayQueue(4)
    loop=True
    while loop:
        print('输入a,添加元素到队列',end=' ')
        print('输入s,显示队列元素',end=' ')
        print('输入g,取出队列头元素',end=' ')
        print('输入h,查看队列头元素',end=' ')
        print('输入e,退出程序')
        print()
        char=input('输入操作类型:')
        if char=='a':
            number=int(input('输入一个数字:'))
            queue.addQueue(number)
        elif char == 'g':
            print(queue.getQueue())
        elif char == 's':
            queue.showQueue()
        elif char == 'h':
            print(queue.headQueue())
        elif char == 'e':
            loop=False
            print('退出程序')




