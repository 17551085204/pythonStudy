#coding=utf-8
#@Author  南柯一梦
#@email   2890241339@qq.com
#@time    2021/3/1 0001   下午 2:30
#import  libs

'''
查找算法
查找某个元素在数组中是否存在，如果存在，返回其所在的索引，如果不存在，返回-1
注意： 如果数组中存在多个该元素，将其所有的索引位置全部返回

1，顺序查找
2, 二分查找，分别使用递归和非递归的方式实现

'''

# 顺序查找
def seqSearch(array,x):
    res=[]
    for i in range(len(array)):
        if array[i]==x:
            res.append(i)
    if res==[]:
        return -1
    else:
        if len(res)==1:
            return res[0]
        else:
            return res


# 二分查找，要求数组是有序的
# 非递归实现
def binarySearch(array,x):
    left=0
    right=len(array)-1
    res=[]
    while left<=right:
        mid=(left+right)//2
        if array[mid]==x:
            for i in range(mid,len(array)):
                if array[i]==x:
                    res.append(i)

            if len(res) == 1:
                return res[0]
            else:
                return res

        elif array[mid]<x:
            left=mid+1
        elif array[mid]>x:
            right=mid-1
    return -1

# 递归实现
def binarySearch2(array,left,right,x):
    if left>right or x<array[0] or x>array[-1]:
        return -1
    mid=(left+right)//2
    # mid=left+(right-left)*(x-array[left])//(array[right]-array[left])
    res=[]
    if array[mid]==x:
        for i in range(mid, len(array)):
            if array[i] == x:
                res.append(i)
        if len(res)==1:
            return res[0]
        else:
            return res
    elif array[mid]<x:
        return binarySearch2(array, mid+1, right, x)
    elif array[mid]>x:
        return binarySearch2(array, left, mid-1, x)



if __name__ == '__main__':
    array=[0,1,2,3,4,5,6,7,8,8]
    val=8
    print(seqSearch(array,val))
    print(binarySearch(array, val))
    print(binarySearch2(array,0,len(array)-1,val))





