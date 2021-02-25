# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/24 15:42         
'''
# import lib


'''
使用栈完成后序表达式(逆波兰表达式)的计算

输入中序表达式-》 转为逆波兰表达式 -》 用逆波兰表达式计算结果

'''

class ArrayStack:
    maxSize = 0  # 栈的大小
    array=[]  # 数组模拟栈，数据放在数组中
    top = -1  # 栈顶，初始为-1
    def __init__(self, maxSize):
        self.maxSize = maxSize
        for i in range(maxSize):
            self.array.append(0)
    # 判断传入的是否是操作符
    def isOper(self, ch):
        if ch in ['-', '+', '*', '/']:
            return True
        else:
            return False
    # 设定操作符的优先级，用数字表示
    def getPrio(self, ch):
        if ch == '+' or ch == '-':
            return 0
        elif ch == '*' or ch == '/':
            return 1

    # 根据传入的操作符合数字计算
    def cal(self, ch, num1, num2):
        if ch == '+':
            return num1 + num2
        elif ch == '-':
            return num1 - num2
        elif ch == '*':
            return num1 * num2
        elif ch == '/':
            return num1 / num2
    # p判断栈满
    def isFull(self):
        return self.top == self.maxSize - 1
    # 判断栈空
    def isEmpty(self):
        return self.top == -1
    # 入栈
    def push(self, x):
        if not self.isFull():
            self.top = self.top + 1
            self.array[self.top] = x
        else:
            print('栈满了，无法入栈')
    # 出栈
    def pop(self):
        if not self.isEmpty():
            res = self.array[self.top]
            self.top = self.top - 1
            return res
        else:
            print('栈已经空了~~')
    # 打印栈中所有元素
    def show(self):
        print('栈中所有元素:')
        for i in range(self.top, -1, -1):
            print(self.array[i])
    # 返回栈顶元素，不是pop
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
            # print('栈为空')

def getStrList(string):
    mylist=list(string)
    opeList=[]
    for i in range(len(mylist)):
        if mylist[i] not in [str(i) for i in range(10)]:
            opeList.append(mylist[i])
            mylist[i]='#'
    numList=''.join(mylist).split('#')
    resList=[0 for i in range(len(numList)+len(opeList))]
    for i in range(0,len(resList),2):
        resList[i]=numList[i//2]
    for i in range(1,len(resList),2):
        resList[i]=opeList[i//2]
    res=[]
    for i in resList:
        if i!='':
            res.append(i)
    return res

# 将传入的中序表达式转为逆波兰表达式    (3+4)*5-19  -->  '3 4 + 5 * 19 -'
def getString(string):
    mylist=string.split(' ')
    myStack=ArrayStack(10)
    resList=[]
    for ch in mylist:
        if ch not in ['+','-','*','/','(',')']: #如果是数字
            resList.append(ch)
        else: # 如果是运算符
            if ch=='(':
                myStack.push(ch)
            elif ch==')':
                while myStack.peek()!='(':
                    resList.append(myStack.pop())
                myStack.pop()       # 消除小括号
            else:
                if myStack.peek()=='(':
                    myStack.push(ch)
                else:
                    while (not myStack.isEmpty()) and (myStack.getPrio(ch)<=myStack.getPrio(myStack.peek())):
                        resList.append(myStack.pop())
                    myStack.push(ch)
    # 最后将myStack中的剩余的全部pop进resList中
    while not myStack.isEmpty():
        resList.append(myStack.pop())
    return resList

# 对于传入的逆波兰表达式进行计算
def cal(strList):
    myStack=ArrayStack(10)
    for ch in strList:
        if ch not in ['+','-','*','/','(',')']: # 如果扫描到数字
            myStack.push(int(ch))
        else:
            num1=myStack.pop()
            num2=myStack.pop()
            res=myStack.cal(ch,num2,num1)
            myStack.push(res)
    # 最后在myStack中的数据就是结果
    return myStack.pop()

if __name__ == '__main__':
    string='(30+4)*5-19'
    string1=' '.join(getStrList(string))
    strList=getString(string1)
    print('{0}={1}'.format(string,cal(strList)))



    


