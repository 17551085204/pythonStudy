# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/3/3 19:25         
'''
# import lib

# 数组实现顺序存储二叉树

class ArrayBinaryTree:
    array=[] # 存储数据的数字
    def __init__(self,array):
        self.array=array

    #  完成顺序存储二叉树的前序遍历
    def preOrder(self,index):# index表示数组的下标
        if self.array==None or len(self.array)==0:
            print('数组为空')
        print(self.array[index])
        # 向左递归
        if 2*index+1<len(self.array):
            self.preOrder(2*index+1)
        # 向右递归
        if 2*index+2<len(self.array):
            self.preOrder(2*index+2)

    #  完成顺序存储二叉树的中序遍历
    def infixOrder(self,index):# index表示数组的下标
        if self.array==None or len(self.array)==0:
            print('数组为空')
        # 向左递归
        if 2*index+1<len(self.array):
            self.infixOrder(2*index+1)
        print(self.array[index])
        # 向右递归
        if 2*index+2<len(self.array):
            self.infixOrder(2*index+2)

    #  完成顺序存储二叉树的后序遍历
    def postOrder(self,index):# index表示数组的下标
        if self.array==None or len(self.array)==0:
            print('数组为空')
        # 向左递归
        if 2*index+1<len(self.array):
            self.postOrder(2*index+1)
        # 向右递归
        if 2*index+2<len(self.array):
            self.postOrder(2*index+2)
        print(self.array[index])

array=[1,2,3,4,5,6,7]
arrayBinaryTree=ArrayBinaryTree(array)
# arrayBinaryTree.preOrder(0)
# arrayBinaryTree.infixOrder(0)
arrayBinaryTree.postOrder(0)
