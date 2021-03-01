# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/28 11:13         
'''
# import lib
 
'''
各种排序算法以及排序速度记录
1，冒泡排序   1w个数据，23.448s
2，选择排序   1w个数据，7.110s
3，插入排序   1w个数据，9.729s
4，希尔排序   交换法实现:1w个数据，34.260s
             移位法实现:1w个数据，141.6ms
5，快速排序   1w个数据，66ms
6, 归并排序   1w个数据，103ms
7，基数排序    1w个数据，40ms

'''
import time
import  numpy as np

class SortDemo:
    # 冒泡排序的实现以及优化
    def bubbleSort(self,array):
        for i in range(len(array)-1): # 代表外层大循环的次数，也就是比较的轮数
            # print('第{}次排序'.format(i+1))
            flag=False
            for j in range(len(array)-1-i): # 每次比较完一轮后，最大的数都会被放到最后，每一轮比较的次数也不断减少
                if array[j]>array[j+1]:
                    flag=True   # 代表这一次大循环里面发生过交换
                    array[j],array[j+1]=array[j+1],array[j]
            if not flag: # 代表此时已经排序好了，不需要继续比较下一轮了
                return

    # 选择排序算法
    def selectSort(self,array):
        for i in range(len(array)-1): # 需要选择的次数
            minVal = array[i] # 将每一轮大循环里面的最小值以及其对应的索引记录下来
            minIndex = i
            for j in range(i+1,len(array)):
                # 每次都找到最小值，需要将其与array[i]交换位置
                if array[j]<=minVal:
                    minVal=array[j]
                    minIndex=j
            if i!=minIndex:  # 只有当i与minIndex不相同时才进行交换，可起到优化作用
                array[i],array[minIndex]=array[minIndex],array[i]

    # 插入排序算法
    def insertSort(self,array):  # 每次都分有序和无序2个部分，然后依次将无序的那部分数据插入到有序部分的合适位置处
        for i in range(len(array)-1):
            insertVal=array[i+1] # 定义待插入的数
            insertIndex=i  # 定义待插入的索引
            # 给insertVal找到插入的位置
            while insertIndex>=0 and insertVal<array[insertIndex]: # 保证数组不越界
                array[insertIndex+1]=array[insertIndex]
                insertIndex=insertIndex-1
            # 推出while循环时，找到了插入的位置
            array[insertIndex+1]=insertVal

    # shell排序,缩小增量的插入排序法
    def shellSort(self,array):
        # 采用交换法实现
        # gap=len(array)//2 # 根据原数组长度设定的初始分组长度
        # while gap>0:
        #     for i in range(gap,len(array)):
        #         #遍历各组中所有元素
        #         j=i-gap
        #         while j>=0:
        #             if array[j]>array[j+gap]:
        #                 array[j],array[j+gap]=array[j+gap],array[j]
        #             j-=gap
        #     gap=gap//2

        # 采用移位法实现
        gap=len(array)//2 # 根据原数组长度设定的初始分组长度
        while gap>0:
            for i in range(gap,len(array)):
                # 采用插入排序的思路
                j=i  # 记录待插入的位置
                temp=array[j] # 待插入的值
                if array[j]<array[j-gap]:
                    while j-gap>=0 and temp<array[j-gap]:
                        array[j]=array[j-gap]
                        j=j-gap
                    # 推出while循环后，就给temp找到了插入的位置
                    array[j]=temp
            gap=gap//2

    # 快速排序算法  对冒泡排序的改进，用空间换时间
    def quickSort(self,array,left,right):
        l=left
        r=right
        pivot=array[(l+r)//2] # 取一个中轴值
        while l<r: # 使得比pivot小的放在其左边，比其大的放在右边
            # 在pivot的左边一直找，直到找到一个大于等于pivot的值
            while array[l]<pivot:
                l+=1
            # 在pivot的有边一直找，直到找到一个小于等于pivot的值
            while array[r]>pivot:
                r-=1
            if l>=r: # 说明pivot的左右两边的值已经符合要求了
                break
            # pivot两边的数值交换
            array[l],array[r]=array[r],array[l]
            # 如果交换完成后,发现array[l]==pivot,需要r--，前移
            if array[l]==pivot:
                r-=1
            # 如果交换完成后,发现array[r]==pivot,需要l++，后移
            if array[r]==pivot:
                l+=1

        # 避免出现栈溢出
        if l==r:
            l=l+1
            r=r-1
        # 下面开始递归
        if left<r:
            self.quickSort(array,left,r)
        if right>l:
            self.quickSort(array,l,right)

    # 归并排序算法
    def merge(self,array,left,mid,right,temp):
        i=left  # 左边有序序列的初始索引
        j=mid+1 # 右边有序序列的初始索引
        t=0  # 作为temp数组的索引
        # 先将左右2边的数据(有序)按照规则填充到temp数组
        # 直到左右2边的有序序列有一方处理完毕为止
        while i<=mid and j<=right:
            # 哪一边的数据更小，就将其填充到temp中，同时其对应的索引+1
            if array[i]<=array[j]:
                temp[t]=array[i]
                t+=1
                i+=1
            else:
                temp[t] = array[j]
                t += 1
                j += 1

        # 把有剩余数据的一方的数据依次全部填充到temp数组
        while i<=mid: # 左边有剩余元素
            temp[t]=array[i]
            t += 1
            i += 1
        while j<=right: # 左边有剩余元素
            temp[t]=array[j]
            t += 1
            j += 1
        # 将temp数组重新拷贝到array
        # 只需要最后拷贝依次即可
        t=0
        tempLeft=left
        while tempLeft<=right:
            array[tempLeft]=temp[t]
            t+=1
            tempLeft+=1
    def mergeSort(self,array,left,right,temp):
        if left<right:
            mid=(left+right)//2
            # 向左递归进行分解
            self.mergeSort(array,left,mid,temp)
            # 向右递归进行分解
            self.mergeSort(array, mid+1,right, temp)
            # 合并
            self.merge(array,left,mid,right,temp)


    # 基数排序算法    准备10个木桶数组，用来存储中间过程
    def radixSort(self,array):
        # array中 最大的数字的位数
        maxVal=0
        for i in range(len(array)):
            if array[i]>maxVal:
                maxVal=array[i]
        length=len(str(maxVal))  # 最大数的位数
        # 初始化水桶数组
        bucket = []
        for i in range(10):
            temp = []
            for j in range(len(array)):
                temp.append(0)
            bucket.append(temp)
        nn=1 # 每次大循环后变为10倍
        for mm in range(length):
            counts=[]              # 用于存放 各个水桶中的数据个数
            for i in range(10):
                counts.append(0)
            # 对每个元素的k位(个,十,百,千,万。。。)进行排序
            for i in range(len(array)):
                element=array[i]//nn%10  # 取出第k位数字
                bucket[element][counts[element]]=array[i]
                counts[element]=counts[element]+1
            index=0
            nn=nn*10
            for k in range(len(counts)):
                # 如果桶中有数据
                if counts[k]!=0:
                    # 循环第k个桶
                    for l in range(counts[k]):
                        array[index]=bucket[k][l]
                        index=index+1

if __name__ == '__main__':
    t1=time.time()
    # 原数组
    maxSize=10
    array=np.random.randint(1,maxSize,size=(1,maxSize))[0]
    temp =np.random.randint(0, 1, size=(1, maxSize))[0]

    print('数组排序前:',array)
    # 创建对象，调用排序算法对数组进行排序
    sortDemo=SortDemo()
    # sortDemo.bubbleSort(array)
    # sortDemo.selectSort(array)
    # sortDemo.insertSort(array)
    # sortDemo.shellSort(array)
    # sortDemo.quickSort(array,0,len(array)-1)
    # sortDemo.mergeSort(array,0,len(array)-1,temp)
    sortDemo.radixSort(array)

    # 打印排序后数组
    t2=time.time()
    print('数组排序后:',array)
    print('排序耗时{}ms'.format((t2-t1)*1000))



