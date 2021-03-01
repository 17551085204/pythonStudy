#coding=utf-8
#@Author  南柯一梦
#@email   2890241339@qq.com
#@time    2021/3/1 0001   下午 2:30
#import  libs

'''
查找算法
查找某个元素在数组中是否存在，如果存在，返回其所在的索引，如果不存在，返回-1

1，顺序查找

'''

# 顺序查找
def seqSearch(array,x):
    for i in range(len(array)):
        if array[i]==x:
            return i
    return -1

# 二分查找，要求数组是有序的
# 非递归实现
def binarySearch(array,x):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            left=mid+1
        elif array[mid]>x:
            right=mid-1
    return -1

# 递归实现  有问题？
def binarySearch2(array,left,right,x):
    if left>right:
        return -1
    mid=(left+right)//2
    if array[mid]==x:
        return mid
    elif array[mid]<x:
        binarySearch2(array, mid+1, right, x)
    elif array[mid]>x:
        binarySearch2(array, left, mid-1, x)





if __name__ == '__main__':
    array=[0,1,2,3,4,5,6,7,8,9]
    print(seqSearch(array,8))
    print(binarySearch(array, 8))
    print(binarySearch2(array,0,len(array)-1,8))




