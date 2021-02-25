# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/24 10:31         
'''
# import lib

class Node:
    num=0
    next=None
    def __init__(self,num):
        self.num=num

#用链表模拟栈
class ListStack:
    head=Node(0)  # 头结点，不是栈的元素
    # 判断栈空,注意，用链表来模拟栈，这时的栈不存在满 的概念
    def isEmpty(self):
        return self.head.next==None
    # 入栈
    def push(self,x):
        temp=Node(x)
        if self.head.next==None: # 对于空栈压入第一个数据
            self.head.next=temp
        else:
            temp.next=self.head.next
            self.head.next=temp

    # 出栈
    def pop(self):
        if not self.isEmpty():
            res= self.head.next.num
            self.head.next=self.head.next.next
            return res
        else:
            print('栈已经空了~~')
    # 打印栈中所有元素
    def show(self):
        print('栈中所有元素:')
        temp=self.head.next
        while temp!=None:
            print(temp.num)
            temp=temp.next







if __name__ == '__main__':
    arrayStack=ListStack()
    loop=True
    while loop:
        print('输入push,入栈', end=' ')
        print('输入pop,出栈', end=' ')
        print('输入show,显示栈中所有数据', end=' ')
        print('输入e,退出程序')
        command=input()
        if command=='e':
            print('程序退出')
            loop=False
        elif command=='push':
            x=int(input('输入一个数'))
            arrayStack.push(x)
        elif command=='pop':
            print(arrayStack.pop())
        elif command=='show':
            arrayStack.show()


