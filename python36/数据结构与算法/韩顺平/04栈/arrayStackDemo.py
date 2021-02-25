# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/24 10:31         
'''
# import lib
 
class ArrayStack:
    maxSize=0  # 栈的大小
    array=[] # 数组模拟栈，数据放在数组中
    top=-1  # 栈顶，初始为-1
    def __init__(self,maxSize):
        self.maxSize=maxSize
        for i in range(maxSize):
            self.array.append(0)
    # 判断传入的是否是操作符
    def isOper(self,ch):
        if ch in ['-','+','*','/']:
            return True
        else:
            return False
    # 设定操作符的优先级，用数字表示
    def getPrio(self,ch):
        if ch=='+' or ch=='-':
            return 0
        elif ch=='*' or ch=='/':
            return 1
    # 根据传入的操作符合数字计算
    def cal(self,ch,num1,num2):
        if ch=='+':
            return num1+num2
        elif ch=='-':
            return num1-num2
        elif ch=='*':
            return num1*num2
        elif ch=='/':
            return num1/num2

    # p判断栈满
    def isFull(self):
        return self.top==self.maxSize-1
    # 判断栈空
    def isEmpty(self):
        return self.top==-1
    # 入栈
    def push(self,x):
        if not self.isFull():
            self.top=self.top+1
            self.array[self.top]=x
        else:
            print('栈满了，无法入栈')
    # 出栈
    def pop(self):
        if not self.isEmpty():
            res=self.array[self.top]
            self.top=self.top-1
            return res
        else:
            print('栈已经空了~~')
    # 打印栈中所有元素
    def show(self):
        print('栈中所有元素:')
        for i in range(self.top,-1,-1):
            print(self.array[i])

    # 返回栈顶元素，不是pop
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print('栈为空')


def add(a,b):
    return a+b



# if __name__ == '__main__':
#     arrayStack=ArrayStack(4)
#     loop=True
#     while loop:
#         print('输入push,入栈', end=' ')
#         print('输入pop,出栈', end=' ')
#         print('输入show,显示栈中所有数据', end=' ')
#         print('输入peek,显示栈顶数据', end=' ')
#         print('输入e,退出程序')
#         command=input()
#         if command=='e':
#             print('程序退出')
#             loop=False
#         elif command=='push':
#             x=int(input('输入一个数'))
#             arrayStack.push(x)
#         elif command=='pop':
#             print(arrayStack.pop())
#         elif command=='show':
#             arrayStack.show()
#         elif command=='peek':
#             print(arrayStack.peek())

