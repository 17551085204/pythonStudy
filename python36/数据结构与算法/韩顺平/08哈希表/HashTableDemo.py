# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/3/1 21:14         
'''
# import lib
 
'''
使用哈希表管理雇员信息
'''

# 雇员类
class Emp:
    id=0
    name=''
    next=None
    def __init__(self,id,name):
        self.id=id
        self.name=name

# Emp组成的链表
class EmpLinkedList:
    # 头指针。指向第一个雇员
    head=None

    # 根据id 删除雇员
    def delEmpByID(self,id):
        if self.head==None:
            return
        if self.head.id==id: # 如果删除的是第一个节点
            self.head=self.head.next
            return
        temp=self.head
        flag=False # 标记该雇员id是否存在
        while True:
            if temp.next==None:
                break
            if temp.next.id==id:
                flag=True
                break
            temp=temp.next
        if flag:
            temp.next=temp.next.next
        else:
            print('id={}的雇员不存在'.format(id))

    # 添加雇员,直接添加到最后
    def add(self,emp):
        if self.head==None:
            self.head=emp
            return
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=emp

    # 根据id 查找雇员
    def findEmpByID(self,id):
        if self.head==None:
            return None
        temp=self.head
        while True:
            if temp.id==id:
                break
            if temp.next==None:
                temp=None
                break
            temp=temp.next
        return temp
    # 遍历链表
    def list(self):
        if self.head==None:
            print('当前链表为空')
        else:
            print('当前链表信息:{',end='')
            temp=self.head
            while temp.next!=None:
                print('({0},{1})-->'.format(temp.id,temp.name),end='')
                temp=temp.next
            print('({0},{1})'.format(temp.id,temp.name),end='}\n')


class HashTable:
    empLinkedListArray=[]
    size=0
    def __init__(self,size):
        self.size=size
        for i in range(size):
            self.empLinkedListArray.append(EmpLinkedList())
    # 哈希函数
    # 这里只是一种最简单的方式
    def hash(self,id):
        return (id-1)%self.size

    # 根据id 删除雇员
    def delEmpByID(self, id):
        num=self.hash(id)
        self.empLinkedListArray[num].delEmpByID(id)

    # 查找雇员
    def findEmpByID(self,id):
        num=self.hash(id)
        return self.empLinkedListArray[num].findEmpByID(id)

    # 添加雇员
    def add(self,emp):
        # 根据id ，判断员工应该被加在哪一条链表
        num=self.hash(emp.id)
        # 将emp加到对应的链表中
        self.empLinkedListArray[num].add(emp)

    # 打印hashTab里面所有的链表
    def list(self):
        count=1
        for empLinkedList in self.empLinkedListArray:
            print('第{}条链表'.format(count),end='==>')
            empLinkedList.list()
            count=count+1



if __name__ == '__main__':
    hashTable=HashTable(4)
    for i in range(1,10):
        hashTable.add(Emp(i,'name={}'.format(i)))
    hashTable.list()
    hashTable.delEmpByID(11)
    print('--------------------------------')
    hashTable.list()



    # loop=True
    # while loop:
    #     print('add:添加雇员 list:显示雇员  exit:退出系统 find:查找雇员')
    #     mystr=input()
    #     if mystr=='add':
    #         id=int(input(('请输入id')))
    #         name=input('请输入名字')
    #         emp=Emp(id,name)
    #         hashTable.add(emp)
    #     elif mystr=='list':
    #         hashTable.list()
    #     elif mystr=='find':
    #         id=int(input('请输入id'))
    #         num=hashTable.hash(id)+1
    #         emp=hashTable.findEmpByID(id)
    #         if emp==None:
    #             print('id={}的雇员不存在'.format(id))
    #         else:
    #             print('该雇员的id={0},姓名为{1},位于第{2}条链表'.format(emp.id,emp.name,num))
    #
    #     elif mystr=='exit':
    #         loop=False




