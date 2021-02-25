# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/24 15:42         
'''
# import lib


'''
使用栈完成中序表达式的计算,只考虑整数的加减乘除运算，没有括号
可以支持多位整数参与计算 

不知为何，一直就存在问题。。。   
最终通过debug发现了问题：numStack与opeStack中的array被共用了，一个修改后会影响另一个的使用

目前将ArrayStack复制了一份，可以解决这个问题，但是方式不好，看看能不能找到更好的办法

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
            print('栈为空')

class ArrayStack2:
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
            print('栈为空')

# 将输入的字符串分割为符合要求的格式
# string='30+1*3-4'
#  设法将这个字符串分割为[30 + 1 * 3 - 4]
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
    return resList

def cal(string):
    strList = getStrList(string)
    numStack = ArrayStack(10)
    opeStack = ArrayStack2(10)
    for ch in strList:
        if opeStack.isOper(ch):  # 如果扫描到操作符
            if not opeStack.isEmpty():  # 如果操作符栈非空
                if opeStack.getPrio(ch) <= opeStack.getPrio(opeStack.peek()):
                    num1 = numStack.pop()
                    num2 = numStack.pop()
                    oper = opeStack.pop()
                    res = numStack.cal(oper, num2, num1)
                    numStack.push(res)
                    opeStack.push(ch)
                else:
                    opeStack.push(ch)
            else:
                opeStack.push(ch)
        else:
            numStack.push(int(ch))
    while not opeStack.isEmpty():
        num1 = numStack.pop()
        num2 = numStack.pop()
        oper = opeStack.pop()
        res = opeStack.cal(oper, num2, num1)
        numStack.push(res)
    return  numStack.pop()



if __name__ == '__main__':
    string='300+1*30-40'
    res=cal(string)
    print('{0}={1}'.format(string, res))




