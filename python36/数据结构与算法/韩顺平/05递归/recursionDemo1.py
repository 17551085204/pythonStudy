# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/25 17:09         
'''
# import lib

# 递归思想的回顾
# 打印问题
def fun1(n):
    if n==0:
        return
    else:
        print(n)
        fun1(n-1)
        print(n)
# fun1(4)
# 阶乘问题
def fun2(n):
    if n==1:
        return 1
    return n*fun2(n-1)
# print(fun2(5))



# 递归的应用1  迷宫
import  numpy as np
'''
说明：map代表地图

(i,j)代表位置，起始 (1,1),结束(6,5)

map(i,j)=0,还没走过
map(i,j)=1,墙
map(i,j)=2,走通
map(i,j)=3,走过但是不通

'''


# map代表地图 i,j代表查找的起始位置
#如果找到通路，返回True,否则返回False
def setWay(map,i,j):
    if map[6][5]==2: # 最后一个点如果变成2了，那么代表此时已经找到了一条通路
        return True
    else:
        if map[i][j]==0:
            # 按照策略走
            map[i][j]=2 #假定这里可以走通
            if setWay(map,i+1,j): # 下
                return  True
            elif setWay(map,i,j+1): # 右
                return  True
            elif setWay(map,i-1,j): # 上
                return  True
            elif setWay(map,i,j-1): # 左
                return  True
            else:
                map[i][j]=3 # 如果到这里，说明假设不成立，走过但是不同
                return False
        else: # 这里map[i][j]只可能是1或3，都是代表不通，所以直接返回False
            return False


def migong():
    map=np.array([[1, 1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  ])
    setWay(map,1,1) # 小球走过并标识过的地图
    print(map)


migong()
