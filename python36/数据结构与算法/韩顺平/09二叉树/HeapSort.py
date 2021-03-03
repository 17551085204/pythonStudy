# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/3/3 21:08         
'''
# import lib
import time
import numpy as np

'''
堆排序算法实现
1w个数据  119ms
'''


# 将一个数组调整为大顶堆
# array:待调整的数组  i:非叶子节点在数组中的索引
# length：逐渐减少
def adjust(array,i,length):
    temp=array[i] # 取出当前元素保存
    k=2*i+1
    while k<length:
        # 左子节点的值小于右子节点的值
        if (k+1<length) and array[k]<array[k+1]:
            k=k+1 # k指向右子节点
        if array[k]>temp:
            array[i]=array[k]
            i=k
        else:
            break
        k=2*k+1
    # 循环结束后，以i为父节点的树的最大值放在了最顶(局部)
    array[i]=temp

# 堆排序
def heapSort(array):
    # 分布测试
    # adjust(array,1,len(array))
    # adjust(array,0,len(array))

    i=len(array)//2-1
    while i>=0:
        adjust(array,i,len(array))
        i=i-1

    for j in range(len(array)-1,0,-1):
        array[j],array[0]=array[0],array[j]
        adjust(array,0,j)


if __name__ == '__main__':
    t1 = time.time()
    # 原数组
    maxSize = 10
    array = np.random.randint(1, maxSize, size=(1, maxSize))[0]
    temp = np.random.randint(0, 1, size=(1, maxSize))[0]
    print('数组排序前:', array)
    heapSort(array)
    # 打印排序后数组
    t2 = time.time()
    print('数组排序后:', array)
    print('排序耗时{}ms'.format((t2 - t1) * 1000))
