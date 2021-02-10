# -*- encoding: utf-8 -*-
'''  
@Author  :   南柯一梦
@Contact :   2890241339@qq.com
2021/1/29 16:23         
'''
# import lib
 
number_list=[2,4,1,7,5,0,8]
index_list=[2,3,4,4,2,5,6,4,0,5,1]
phone_nmuber_list=[str(number_list[i]) for i in index_list]
phone_nmuber=''.join(phone_nmuber_list)
print(phone_nmuber)
