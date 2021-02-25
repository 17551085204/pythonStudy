# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/21 22:04         
'''
# import lib

# 节点类, 用于实现双向链表
class HeroNode:
    no=0
    name=''
    nickname=''
    next=None
    pre=None
    def __init__(self,no,name,nickname):
        self.no=no
        self.name=name
        self.nickname=nickname

    def show(self):
        print('HeroNode:no={0},name={1},nickname={2}'.format(self.no,self.name,self.nickname))


# 双向链表类，管理节点
class DoubleLinkedList:
    # 初始化一个头结点，不进行修改，不存放具体数据
    head=HeroNode(0,'head_name','head_nickname')

    # 根据no修改链表中某一节点的信息,如果找到该节点，修改节点的name和nickname为指定的值，如果找不到该节点
    # 输出节点不存在
    def update(self,no,name,nickname):
        temp = self.head
        flag = False  # 标记是否存在该节点
        while True:
            if temp.next == None:
                break
            if temp.next.no == no:
                flag = True
                break
            temp = temp.next
        if flag:
            temp.next.name=name
            temp.next.nickname=nickname
        else:
            print('no={}的节点不存在'.format(no))

    # 根据no打印链表中某一节点的信息
    def find(self,no):
        temp=self.head
        flag=False # 标记是否存在该节点
        while True:
            if temp.next==None:
                break
            if temp.next.no==no:
                flag=True
                break
            temp=temp.next
        if flag:
            temp.next.show()
        else:
            print('no={}的节点不存在'.format(no))

    #双向链表中添加节点,直接添加至链表的最后
    def add(self,heroNode):
        temp=self.head
        flag=False
        while True:
            if temp.next==None:
                break
            if temp.next.no==heroNode.no:
                flag=True
                break
            temp=temp.next
        # 将节点加入末尾
        if flag:
            print('no={}的节点已经存在'.format(heroNode.no))
        else:
            temp.next=heroNode
            heroNode.pre=temp


    # 单链表中添加节点,按照添加节点的no大小，从小到大加入链表
    def addByOrder(self, heroNode):
        temp=self.head
        flag=False # 标记是否已经存在这个no
        while True:
            if temp.next==None:
                break
            if temp.next.no>heroNode.no: # temp后面就是要插入的位置
                break
            if temp.next.no==heroNode.no:
                flag=True
                break
            temp=temp.next

        if flag:
            print('no={}的节点已经存在'.format(heroNode.no))
        else:
            heroNode.next=temp.next
            if temp.next!=None:
                temp.next.pre=heroNode
            temp.next=heroNode
            heroNode.pre=temp


    # 双向链表，根据no删除节点,如果有这个no就可以删除，如果没有，打印 no不存在
    def delete(self,no):
        temp=self.head
        flag=False # 默认没有no节点
        while True:
            if temp.next==None:
                break
            if temp.next.no==no:
                flag=True
                break
            temp=temp.next
        if flag:# 开始删除节点
            temp.next=temp.next.next
            if temp.next!=None:
                temp.next.pre=temp
        else:
            print('no={}的节点不存在'.format(no))


    # 获取链表长度
    def size(self):
        count=0
        temp=self.head
        while temp.next!=None:
            count=count+1
            temp=temp.next
        return count

    # 打印双向链表中所有节点
    def show(self):
        if self.head.next==None:
            print('双向链表为空')
            return
        print('所有节点有:\n{')
        temp=self.head.next
        while True:
            temp.show()
            temp=temp.next
            if temp==None:
                break
        print('}')

    # 查找双向链表中倒数第k个节点,打印出信息
    def findRevK(self,k):
        length = self.size()
        if 1<=k<=length:
            temp=self.head
            for i in range(length-k+1):
                temp=temp.next
            temp.show()
        else:
            print('k可能小于1或者大于链表长度:{}'.format(length))

    # 双向链表的翻转
    def reverseList(self):
        # 如果链表长度为0或1，不需要翻转
        if self.head.next==None or self.head.next.next==None:
            return
        newHead=HeroNode(-1,'','')
        temp=self.head.next
        while temp!=None:
            nextNode = temp.next
            temp.next=newHead.next
            if newHead.next!=None:
                newHead.next.pre=temp
            newHead.next=temp
            temp.pre=newHead
            temp=nextNode
        self.head.next=newHead.next


    # 打印链表中第index个节点
    def  printKList(self,index):
        temp=self.head
        for i in range(index):
            temp=temp.next
        temp.show()

    # 从尾到头打印单链表
    def printRevList(self):
        length=self.size()
        for i in range(length,0,-1):
            self.printKList(i)









if __name__ == '__main__':
    doubleLinkedList=DoubleLinkedList()
    # doubleLinkedList.add(HeroNode(1,'宋江','及时雨'))
    # doubleLinkedList.add(HeroNode(3, '吴用', '智多星'))
    # doubleLinkedList.add(HeroNode(2, '卢俊义', '玉麒麟'))

    doubleLinkedList.addByOrder(HeroNode(4, '武松', '行者'))
    doubleLinkedList.addByOrder(HeroNode(1, '宋江', '及时雨'))
    doubleLinkedList.addByOrder(HeroNode(3, '吴用', '智多星'))
    doubleLinkedList.addByOrder(HeroNode(2, '卢俊义', '玉麒麟'))

    # doubleLinkedList.update(3,'wuyong','zhiduoxing')
    # doubleLinkedList.delete(4)
    # doubleLinkedList.find(4)
    # print('双向链表中节点总数为:{}'.format(doubleLinkedList.size()))
    # doubleLinkedList.findRevK(4)
    # doubleLinkedList.printRevList()
    # doubleLinkedList.reverseList()

    doubleLinkedList.show()

