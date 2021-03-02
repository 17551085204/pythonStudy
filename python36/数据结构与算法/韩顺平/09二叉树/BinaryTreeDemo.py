# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/3/2 19:26         
'''
# import lib
 
'''
二叉树


'''

# 创建节点
class HeroNode:
    id=0
    name=''
    left=None
    right=None
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def show(self):
        print('id={0},name={1}'.format(self.id,self.name))

    # 删除节点的方法
    # 如果是叶子节点，直接删除，如果不是叶子节点，那么直接删除该节点下面的子树
    def delNode(self,id):
        if self.left!=None and self.left.id==id:
            self.left=None
            return
        if self.right!=None and self.right.id==id:
            self.right=None
            return
        if self.left!=None:
            self.left.delNode(id)
        if self.right != None:
            self.right.delNode(id)


    # 前序查找的方法,找到就返回该id 对应的节点，否则返回None
    def preSearch(self,id):
        print('前序查找')
        if self.id==id:
            return self
        resNode=None # 保存查找到的结果节点
        if self.left!=None:
            resNode = self.left.preSearch(id)
        if resNode!=None:
            return resNode
        else:
            if self.right!=None:
                resNode=self.right.preSearch(id)
            return resNode

    # 中序查找的方法,找到就返回该id 对应的节点，否则返回None
    def infixSearch(self, id):
        resNode = None  # 保存查找到的结果节点
        if self.left != None:
            resNode = self.left.infixSearch(id)
        if resNode != None:
            return resNode
        print('中序查找')
        if self.id == id:
            return self
        if self.right != None:
            resNode = self.right.infixSearch(id)
        return resNode

    # 后序查找的方法,找到就返回该id 对应的节点，否则返回None
    def postSearch(self, id):
        resNode = None  # 保存查找到的结果节点
        if self.left != None:
            resNode = self.left.postSearch(id)
        if resNode != None:
            return resNode
        if self.right != None:
            resNode = self.right.postSearch(id)
        if resNode != None:
            return resNode
        print('后序查找')
        if self.id == id:
            return self
        else:
            return None

    # 前序遍历的方法
    def preOrder(self):
        self.show()
        # 递归左子树遍历
        if self.left!=None:
            self.left.preOrder()
        # 递归右子树遍历
        if self.right!=None:
            self.right.preOrder()

    # 中序遍历的方法
    def infixOrder(self):
        # 递归左子树遍历
        if self.left!=None:
            self.left.infixOrder()
        self.show()
        # 递归右子树遍历
        if self.right!=None:
            self.right.infixOrder()

    # 后序遍历的方法
    def postOrder(self):
        # 递归左子树遍历
        if self.left!=None:
            self.left.postOrder()
        # 递归右子树遍历
        if self.right!=None:
            self.right.postOrder()
        self.show()


# 创建二叉树
class BinaryTree:
    root=None # 根节点
    def setRoot(self,root):
        self.root=root

    # 删除节点
    def delNode(self,id):
        if self.root!=None:
            if self.root.id==id:
                self.root=None
            else:
                self.root.delNode(id)
        else:
            print('空树，不可以删除')
    # 前序查找的方法
    def preSearch(self,id):
        if self.root != None:
            return self.root.preSearch(id)
        else:
            print('二叉树为空')

    # 中序查找的方法
    def infixSearch(self,id):
        if self.root != None:
            return self.root.infixSearch(id)
        else:
            print('二叉树为空')

    # 后序查找的方法
    def postSearch(self,id):
        if self.root != None:
            return self.root.postSearch(id)
        else:
            print('二叉树为空')


    # 前序遍历的方法
    def preOrder(self):
        if self.root!=None:
            self.root.preOrder()
        else:
            print('二叉树为空')
    # 中序遍历的方法
    def infixOrder(self):
        if self.root!=None:
            self.root.infixOrder()
        else:
            print('二叉树为空')
    # 后序遍历的方法
    def postOrder(self):
        if self.root!=None:
            self.root.postOrder()
        else:
            print('二叉树为空')


if __name__ == '__main__':
    # 创建节点
    node1 = HeroNode(1,'宋江')
    node2 = HeroNode(2, '吴用')
    node3 = HeroNode(3, '卢俊义')
    node4 = HeroNode(4,'林冲')
    node5 = HeroNode(5, '关胜')
    node1.left=node2
    node1.right=node3
    node3.right=node4
    node3.left=node5
    # 创建一棵二叉树
    binaryTree=BinaryTree()
    binaryTree.setRoot(node1)
    binaryTree.delNode(3)  # 删除某一节点


    ###### 前中后序遍历
    # print('前序遍历')
    # binaryTree.preOrder()
    # print('中序遍历')
    # binaryTree.infixOrder()
    # print('后序遍历')
    # binaryTree.postOrder()

    ###### 根据id 查找节点
    # id=5
    # resNode=binaryTree.postSearch(id)
    # # resNode = binaryTree.infixSearch(id)
    # # resNode = binaryTree.preSearch(id)
    # if resNode!=None:
    #     resNode.show()
    # else:
    #     print('没有id={}的节点'.format(id))



