# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/23 20:30         
'''
# import lib
 

# 约瑟夫环问题，单向环形链表


class Boy:
    id=0
    next=None
    def __init__(self,id):
        self.id=id

class CircleList:
    first=Boy(-1) # 创建第一个boy节点
    # 将num 个小孩加入环形链表中
    def addBoy(self,num):
        if num<2:
            print('输入的num值有误')
            return
        curBoy=None
        #通过循环，构建出环形链表
        for i in range(1,num+1):
            boy=Boy(i)
            if i==1: # 第一个小孩
                self.first=boy
                self.first.next=self.first
                curBoy=self.first
            else:
                curBoy.next=boy
                boy.next=self.first
                curBoy=boy

    def showBoy(self):
        if self.first==None:
            print('链表为空')
            return
        curBoy=self.first
        while True:
            print('Boy,id={}'.format(curBoy.id))
            if curBoy.next==self.first:
                break
            curBoy=curBoy.next

    '''
    从第几个小孩开始数，每次数几个，链表中原有几个小孩
    '''
    def countBoy(self,startNo,countNum,nums):
        self.addBoy(nums)
        if self.first==None or startNo<1 or startNo>nums:
            print('输入数据不合理')
            return
        helper=self.first
        while True:
            if helper.next==self.first: # helper指向最后一个节点
                break
            helper=helper.next
        # 报数前，helper和first移动statNo次
        for i in range(startNo-1):
            helper=helper.next
            self.first=self.first.next
        # 小孩报数
        while True:
            if helper==self.first: # 此时只有一个节点
                break
            for i in range(countNum-1):
                helper = helper.next
                self.first = self.first.next
            print('id={}的小孩出圈'.format(self.first.id))
            # 将first指向的节点移除循环链表
            self.first=self.first.next
            helper.next=self.first
        print('id={}的小孩出圈'.format(self.first.id))


if __name__ == '__main__':
    circleList=CircleList()
    # circleList.addBoy(5)
    # circleList.showBoy()
    circleList.countBoy(1,5,100)





