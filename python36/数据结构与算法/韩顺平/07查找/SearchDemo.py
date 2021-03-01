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
            temp = mid - 1
            while array[mid] == x:
                res.append(mid)
                mid = mid + 1
                if mid >= len(array):
                    break
            while array[temp] == x:
                res.append(temp)
                temp = temp - 1
                if temp < 0:
                    break
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
    # mid=(left+right)//2  # 二分查找
    # 插值查找
    mid=left+(right-left)*(x-array[left])//(array[right]-array[left])

    res=[]
    if array[mid]==x:
        temp=mid-1
        while array[mid]==x:
            res.append(mid)
            mid=mid+1
            if mid >= len(array):
                break
        while array[temp]==x:
            res.append(temp)
            temp=temp-1
            if temp <0:
                break


        if len(res)==1:
            return res[0]
        else:
            return res
    elif array[mid]<x:
        return binarySearch2(array, mid+1, right, x)
    elif array[mid]>x:
        return binarySearch2(array, left, mid-1, x)

# 斐波那契查找算法
# 返回斐波那契数组的第k个元素
def fib(k):
    if k==1 or k==2:
        return 1
    return fib(k-1)+fib(k-2)
# 斐波那契数组查找算法
def fibSearch(array,x):
    left = 0
    right = len(array) - 1
    k=1 # 斐波那契分割数值对应的序号
    res=[]
    while right>fib(k)-1:
        k=k+1
    temp=[]
    for i in array:
        temp.append(i)
    for i in range(fib(k)-len(array)):
        temp.append(array[-1])

    while left<=right:
        mid=left+fib(k-1)-1
        if x<temp[mid]:
            right=mid-1
            k=k-1
        elif x>temp[mid]:
            left=mid+1
            k=k-2
        else:
            if right<=mid:
                mid=right

            te = mid - 1
            while array[mid] == x:
                res.append(mid)
                mid = mid + 1
                if mid >= len(array):
                    break
            while array[te] == x:
                res.append(te)
                te = te - 1
                if te < 0:
                    break
            if len(res) == 1:
                return res[0]
            else:
                return res


if __name__ == '__main__':
    array=[0,1,2,3,4,5,6,7,8,8,8]
    val=8
    print(seqSearch(array,val))
    print(binarySearch(array, val))
    print(binarySearch2(array,0,len(array)-1,val))
    print(fibSearch(array,val))





