# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/21 22:04         
'''
# import lib

# 节点类
class HeroNode:
    no=0
    name=''
    nickname=''
    next=None
    def __init__(self,no,name,nickname):
        self.no=no
        self.name=name
        self.nickname=nickname

    def show(self):
        print('HeroNode:no={0},name={1},nickname={2}'.format(self.no,self.name,self.nickname))


# 单链表类，管理节点
class SingleLinkedList:
    # 初始化一个头结点，不进行修改，不存放具体数据
    head=HeroNode(0,'head_name','head_nickname')

    # 根据no修改链表中某一节点的信息,如果找到该节点，修改节点的name和nickname为指定的值，如果找不到该节点
    # 输出节点不存在
    def update(self,no,name,nickname):
        temp = self.head.next
        length = self.size()
        isFinded = False
        for i in range(length):
            if temp.no == no:
                isFinded = True
                break
            else:
                temp = temp.next
        if isFinded:
            temp.name=name
            temp.nickname=nickname
        else:
            print('不存在no={}的节点'.format(no))


    # 根据no打印链表中某一节点的信息
    def find(self,no):
        temp=self.head.next
        length=self.size()
        isFinded=False
        for i in range(length):
            if temp.no==no:
                isFinded=True
                break
            else:
                temp=temp.next
        if isFinded:
            temp.show()
        else:
            print('不存在no={}的节点'.format(no))


    #单链表中添加节点,直接添加至链表的最后
    def add(self,heroNode):
        temp=self.head
        flag = False  # flag标志添加的编号是否存在，默认为false
        while temp.next!=None:
            if temp.next == None: #说明temp已经在链表的最后
                break
            if temp.next.no==heroNode.no:
                flag=True
                break
            temp=temp.next
        if flag:
            print('编号no={}已经存在'.format(heroNode.no))
        else:
            temp.next=heroNode

    # 单链表中添加节点,按照添加节点的no大小，从小到大加入链表
    def addByOrder(self, heroNode):
        # 因为头节点不能动，因此我们仍然通过一个辅助指针(变量)
        # 来帮助找到添加的位置
        # 因为单链表，因为我们找的temp
        # 是位于
        # 添加位置的前一个节点，否则插入不了
        temp = self.head
        flag = False #flag标志添加的编号是否存在，默认为false
        while True:
            if temp.next == None: #说明temp已经在链表的最后
                break
            if temp.next.no > heroNode.no:#  位置找到，就在temp的后面插入
                break
            elif temp.next.no == heroNode.no: # 说明希望添加的heroNode的编号已然存在
                flag = True # 说明编号存在
                break
            temp = temp.next  # 后移，遍历当前链表
        if flag:
            print('编号no={}已经存在'.format(heroNode.no))
        else:
            heroNode.next = temp.next
            temp.next = heroNode


    # 单链表，根据no删除节点,如果有这个no就可以删除，如果没有，打印 no不存在
    def delete(self,no):
        temp=self.head
        if temp.next==None:
            print('链表为空，无法删除节点')
        else:
            while True:
                if temp.next != None:
                    if temp.next.no==no:
                         temp.next=temp.next.next
                         break
                    else:
                        temp = temp.next
                else:
                    print('不存在no={}的节点'.format(no))
                    break

    # 单链表，根据no删除节点,如果有这个no就可以删除，如果没有，打印 no不存在
    # 下面是第二种删除节点的方法，思路更加清晰
    def delete2(self,no):
        flag=False # 代表是否有传入的节点
        temp=self.head
        while True:
            if temp.next==None:
                break
            if temp.next.no==no:
                flag=True # 代表找到了temp就是要删除节点的前一个节点
                break
            temp=temp.next
        if flag:
            temp.next=temp.next.next
        else:
            print('no={}的节点不存在，无法删除'.format(no))

    # 获取链表长度
    def size(self):
        count=0
        temp=self.head.next
        while temp!=None:
            count=count+1
            temp=temp.next
        return count

    # 打印单链表中所有节点
    def show(self):
        print('链表中所有节点信息\n{')
        temp=self.head.next
        while temp!=None:
            temp.show()
            temp=temp.next
        print('}')

    # 查找单链表中倒数第k个节点,打印出信息
    def findRevK(self,k):
        length=self.size()
        if not (1<=k<=length): # 如果k的输入不符合规范
            print('k值输入不规范，可能小于了数字1或者超出了单链表的节点个数:{},'.format(length))
            return
        temp=self.head
        if self.head.next==None:
            print('链表为空')
            return
        else:
            for i in range(length-k+1):
                temp=temp.next
            temp.show()

    # 单链表的翻转
    def reverseList(self):
        reverseHead = HeroNode(-1, '', '')
        if self.head.next==None or self.head.next.next==None: # 对于空链表和长度为1的链表单独处理
            return
        cur=self.head.next # 扫描到的当前节点
        while cur!=None:
            nextNode = cur.next  # 当前节点的下一个节点
            cur.next=reverseHead.next
            reverseHead.next=cur
            cur=nextNode
        self.head.next = reverseHead.next

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

    # 合并2个链表，有时间再看吧。。。







if __name__ == '__main__':
    singleLinkedList=SingleLinkedList()
    # singleLinkedList.add(HeroNode(1,'宋江','及时雨'))
    # singleLinkedList.add(HeroNode(3, '吴用', '智多星'))
    # singleLinkedList.add(HeroNode(2, '卢俊义', '玉麒麟'))
    # singleLinkedList.add(HeroNode(2, '卢俊义~', '玉麒麟'))

    # singleLinkedList.delete(2)
    # print('单链表长度为:{}'.format(singleLinkedList.size()))
    # singleLinkedList.find(11)
    # singleLinkedList.update(1,'songjiang','jishiyu')
    # singleLinkedList.update(3, 'wuyong', 'zhiduoxing')
    # singleLinkedList.update(4, 'lujunyi', 'yuqiling')

    singleLinkedList.addByOrder(HeroNode(4, '武松', '行者'))
    singleLinkedList.addByOrder(HeroNode(1, '宋江', '及时雨'))
    singleLinkedList.addByOrder(HeroNode(3, '吴用', '智多星'))
    singleLinkedList.addByOrder(HeroNode(2, '卢俊义', '玉麒麟'))
    singleLinkedList.addByOrder(HeroNode(5, '林冲', '豹子头'))

    # singleLinkedList.reverseList()

    # singleLinkedList.find(4)
    # singleLinkedList.delete2(1)

    # singleLinkedList.findRevK(4)

    # print('单链表中节点个数size={}'.format(singleLinkedList.size()))
    # singleLinkedList.show()

    # 逆序打印，不改变链表
    # singleLinkedList.printRevList()
    # singleLinkedList.show()
