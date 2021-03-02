# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10411 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 采用暴力法解决
        # res=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             res.append(i)
        #             res.append(j)
        #             return res

        # 采用哈希表的方式解决
        res=[]
        map={}
        for i in range(len(nums)):
            map[nums[i]]=i
        for j in range(len(nums)):
            diff=target-nums[j]
            if (diff in map) and (map[diff]!=j):
                res.append(j)
                res.append(map[diff])
                return res



# leetcode submit region end(Prohibit modification and deletion)
