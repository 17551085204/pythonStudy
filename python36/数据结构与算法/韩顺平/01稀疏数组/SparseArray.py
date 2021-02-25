# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/2/16 10:17         
'''
# import lib
import pickle

#  数组转为稀疏数组
def array2sparse(array):
    hang=len(array)
    lie=len(array[0])
    sparseArray=[]
    count=0 # 记录有多少个非零元素
    for i in range(hang):
        for j in range(lie):
            if array[i][j]!=0:
                count=count+1
                temp=[i,j,array[i][j]]
                sparseArray.append(temp)
    sparseArray=[[hang,lie,count]]+sparseArray
    return sparseArray

# 稀疏数组转为数组
def sparse2array(sparseArray):
    # 数组的行和列数
    hang=sparseArray[0][0]
    lie =sparseArray[0][1]
    array=[]
    for j in range(hang):
        temp=[]  #注意，这里的temp要定义在循环里面，因为会有浅拷贝的问题
        for i in range(lie):
            temp.append(0)
        array.append(temp)
    for k in range(1,len(sparseArray)):
        a = sparseArray[k][0]
        b = sparseArray[k][1]
        c = sparseArray[k][2]
        array[a][b]=c
    return array

# 主程序入口
def main():
    # 原始数组
    array=[[1,0,0,0,0],[0,2,0,0,0],[0,0,0,0,1]]
    print('原数组:\n', array)
    # 转为稀疏数组
    sparseArray=array2sparse(array)
    print('对应的稀疏数组:\n',sparseArray)
    # 将稀疏数组序列化保存
    sfile = open("sparse.dat", "wb")
    pickle.dump(sparseArray, sfile)
    sfile.close()
    # 读取序列化数据，还原数组
    dfile = open("sparse.dat", "rb")
    sparseArray_load = pickle.load(dfile)
    dfile.close()
    array_new=sparse2array(sparseArray_load)
    print('还原为原数组:\n',array_new)
    print('\n原数组与还原得到的数组是否相同:\n',array==array_new)


if __name__=='__main__':
    main()



