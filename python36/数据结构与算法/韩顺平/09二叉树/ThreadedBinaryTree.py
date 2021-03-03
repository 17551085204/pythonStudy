# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/3/3 19:44         
'''
# import lib
 
# 线索化二叉树


# 创建节点
class HeroNode:
    id=0
    name=''
    left=None
    right=None
    leftType  = 0  # 0代表指向左子树，2代表指向前驱节点
    rightType = 0  # 0代表指向右子树，2代表指向后继节点

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


# 实现了线索化功能的二叉树
class ThreadedBinaryTree:
    root=None # 根节点
    # 为了实现线索化，需要一个指向当前节点的指针pre
    pre=None

    def setRoot(self,root):
        self.root=root

    # 中序线索化之后遍历二叉树
    def threadedList(self):
        node =self.root
        while node !=None:
            # 找到第一个leftType=1的节点
            while node.leftType==0:
                node=node.left
            node.show()
            # 如果当前节点的右指针是后继节点
            while node.rightType==1:
                node=node.right
                node.show()
            # 替换遍历的节点
            node=node.right


    # 对二叉树进行中序线索化
    def threadedNodes(self,node):
        # 对传入的node节点进行线索化
        if node==None:
            return
        # 线索化左子树
        self.threadedNodes(node.left)

        # 线索化当前节点
        # 处理当前节点的前驱节点
        if node.left==None:
            node.left=self.pre
            node.leftType=1  # 左指针指向前驱节点
        # 处理当前节点的后继节点
        if self.pre!=None and self.pre.right==None:
            self.pre.right=node
            self.pre.rightType=1# 前驱节点的右指针指向当前节点
        self.pre=node # 很重要
        # 线索化右子树
        self.threadedNodes(node.right)


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
    node1 = HeroNode(1, '宋江')
    node2 = HeroNode(3, '吴用')
    node3 = HeroNode(6, '卢俊义')
    node4 = HeroNode(8, '林冲')
    node5 = HeroNode(10, '关胜')
    node6 = HeroNode(14, '武松')

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    # 创建一棵二叉树
    binaryTree = ThreadedBinaryTree()
    binaryTree.setRoot(node1)
    print('线索化之前中序遍历')
    binaryTree.infixOrder()
    print('----------------------------------')
    # 线索化二叉树
    binaryTree.threadedNodes(node1)

    # 中序线索化后遍历
    print('中序线索化后遍历')
    binaryTree.threadedList()


    # 线索化之前与之后的区别
    # if node4.right!=None:
    #     node4.right.show()
    # else:
    #     print('node4的右指针没有连接其他节点')




